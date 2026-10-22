"""Convert the pinned SOB text test split into self-contained Harbor tasks."""

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "vendor"))

from sob.common.prompts import SYSTEM_PROMPT, build_user_message  # noqa: E402
from sob.common.serialization import build_eval_record  # noqa: E402
from utils.utils import parse_string  # noqa: E402


def generate_task(record: dict, output: Path, index: int) -> Path:
    # Upstream record_id is not unique; retain every row of the pinned split.
    name = f"sob-text-{index:05d}"
    task = output / name
    task.mkdir()
    for directory in ("environment", "tests", "solution"):
        (task / directory).mkdir()
    for source, target in (
        ("task.toml", "task.toml"),
        ("Dockerfile", "environment/Dockerfile"),
        ("test.sh", "tests/test.sh"),
        ("verify.py", "tests/verify.py"),
        ("solve.sh", "solution/solve.sh"),
    ):
        shutil.copyfile(ROOT / "template" / source, task / target)
    shutil.copyfile(ROOT / "vendor/evaluate.py", task / "tests/evaluate.py")
    instruction = (
        "Use the following extraction rules and source material. "
        "Write your final JSON object to `/tmp/answer.json`. "
        "The verifier reads that file, not your final chat message.\n\n"
        + SYSTEM_PROMPT
        + "\n\n"
        + build_user_message(record)
        + "\n"
    )
    (task / "instruction.md").write_text(instruction, encoding="utf-8")
    evaluation = build_eval_record(record, None, "harbor-agent", "text", 0, 0, 0)
    (task / "tests/record.json").write_text(
        json.dumps(evaluation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (task / "solution/answer.json").write_text(
        json.dumps(parse_string(record["ground_truth"]), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return task


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / ".cache/test.parquet")
    parser.add_argument("--output", type=Path, default=ROOT / "tasks")
    args = parser.parse_args()
    source = json.loads((ROOT / "provenance.json").read_text())["dataset"]
    if not args.data.exists():
        args.data.parent.mkdir(parents=True, exist_ok=True)
        url = f"{source['repository']}/resolve/{source['revision']}/{source['path']}"
        with urlopen(url, timeout=120) as response, args.data.open("wb") as stream:
            shutil.copyfileobj(response, stream)
    with args.data.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    if digest != source["sha256"]:
        raise ValueError(f"dataset checksum mismatch: {args.data}")
    from pyarrow import parquet

    rows = parquet.read_table(args.data).to_pylist()
    if len(rows) != source["task_count"]:
        raise ValueError(f"expected {source['task_count']} records, got {len(rows)}")
    args.output.mkdir(parents=True, exist_ok=False)
    tasks = [generate_task(record, args.output, index).name for index, record in enumerate(rows)]
    catalog = (
        'name = "sob-text"\nversion = "1.0.0"\n'
        'description = "SOB text test split with agent-produced JSON and upstream metrics."\n'
        'task_directory = "sob-text"\nprimary_metric = "reward"\n\ntasks = [\n'
        + "".join(f'  "{name}",\n' for name in tasks)
        + "]\n"
    )
    (args.output.parent / "dataset.toml").write_text(catalog)
    print(f"Generated {len(rows)} tasks in {args.output}")


if __name__ == "__main__":
    main()
