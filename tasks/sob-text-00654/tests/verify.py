import argparse
import json
from pathlib import Path

from evaluate import METRIC_DISPLAY_NAMES, evaluate_record


def verify(record_path: Path, answer_path: Path, output: Path) -> dict[str, float]:
    record = json.loads(record_path.read_text())
    try:
        candidate = json.loads(answer_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, UnicodeDecodeError, json.JSONDecodeError):
        candidate = None
    record["output"]["candidate_response"] = candidate
    evaluated = evaluate_record(record, "text")
    rewards = {key: evaluated.row[key] for key in METRIC_DISPLAY_NAMES}
    rewards["reward"] = rewards["leaf_value_em"]
    output.mkdir(parents=True, exist_ok=True)
    (output / "reward.json").write_text(json.dumps(rewards, indent=2) + "\n")
    (output / "eval_record.json").write_text(
        json.dumps(
            {
                **evaluated.row,
                "missing_gt_paths": evaluated.missing_gt_paths,
                "missing_required_paths": evaluated.missing_required_paths,
            },
            indent=2,
        )
        + "\n"
    )
    return rewards


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate an agent's JSON with the pinned SOB scorer."
    )
    parser.add_argument("--record", type=Path, default=Path("/tests/record.json"))
    parser.add_argument("--answer", type=Path, default=Path("/tmp/answer.json"))
    parser.add_argument("--output", type=Path, default=Path("/logs/verifier"))
    args = parser.parse_args()
    verify(args.record, args.answer, args.output)
