import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from convert import ROOT, generate_task

sys.path.insert(0, str(ROOT / "vendor"))
from evaluate import evaluate_record  # noqa: E402

spec = importlib.util.spec_from_file_location("sob_verify", ROOT / "template/verify.py")
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class ConversionTest(unittest.TestCase):
    def test_generated_task_and_upstream_scoring(self):
        record = {
            "record_id": "sample",
            "context": "Ada bought 2 books.",
            "question": "Who bought books and how many?",
            "json_schema": json.dumps(
                {
                    "type": "object",
                    "properties": {"name": {"type": "string"}, "count": {"type": "integer"}},
                    "required": ["name", "count"],
                    "additionalProperties": False,
                }
            ),
            "ground_truth": json.dumps({"name": "Ada", "count": 2}),
            "schema_complexity": "easy",
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            task = generate_task(record, root, 0)
            second = generate_task(record, root, 1)
            self.assertNotEqual(task, second)
            self.assertEqual(
                (task / "tests/record.json").read_bytes(),
                (second / "tests/record.json").read_bytes(),
            )
            self.assertIn(record["context"], (task / "instruction.md").read_text())
            self.assertEqual(
                (task / "tests/evaluate.py").read_bytes(),
                (ROOT / "vendor/evaluate.py").read_bytes(),
            )
            answer = root / "answer.json"
            output = root / "result"
            for candidate, score, valid in (
                ('{"name": "Ada", "count": 2}', 1.0, 1.0),
                ('{"name": "Ada", "count": 3}', 0.5, 1.0),
                ('{"name": "Ada", "count": "2"}', 0.0, 0.0),
                ('{"name": "Ada"}', 0.0, 0.0),
                ('```json\n{"name": "Ada", "count": 2}\n```', 0.0, 0.0),
                (None, 0.0, 0.0),
            ):
                with self.subTest(candidate=candidate):
                    if candidate is None:
                        answer.unlink(missing_ok=True)
                    else:
                        answer.write_text(candidate)
                    rewards = verifier.verify(task / "tests/record.json", answer, output)
                    self.assertEqual(rewards["reward"], score)
                    self.assertEqual(rewards["schema_compliance"], valid)
                    self.assertEqual(rewards, json.loads((output / "reward.json").read_text()))

            answer.write_bytes((task / "solution/answer.json").read_bytes())
            subprocess.run(
                [
                    sys.executable,
                    str(task / "tests/verify.py"),
                    "--record",
                    str(task / "tests/record.json"),
                    "--answer",
                    str(answer),
                    "--output",
                    str(output),
                ],
                check=True,
            )
            rewards = json.loads((output / "reward.json").read_text())
            self.assertEqual(rewards["reward"], 1.0)

    def test_real_conversion_preserves_reference_scores(self):
        tasks = sorted((ROOT / "tasks").glob("*/tests/record.json"))
        if not tasks:
            self.skipTest("run convert.py to check the complete converted dataset")
        self.assertEqual(len(tasks), 5000)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            for record_path in tasks:
                record = json.loads(record_path.read_text())
                answer = record_path.parent.parent / "solution/answer.json"
                record["output"]["candidate_response"] = json.loads(answer.read_text())
                expected = evaluate_record(record, "text").row
                rewards = verifier.verify(record_path, answer, output)
                self.assertEqual(rewards["reward"], expected["leaf_value_em"])
                self.assertEqual(rewards["strict_json_em"], expected["strict_json_em"])


if __name__ == "__main__":
    unittest.main()
