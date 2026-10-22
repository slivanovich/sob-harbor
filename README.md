# SOB For Harbor

The 5,000-record text test split of [InterfazeAI/SOB](https://github.com/InterfazeAI/sob),
converted into Harbor tasks. Each task supplies the original context, question
and JSON schema. The agent writes `/tmp/answer.json`; the verifier evaluates it
using the pinned upstream `evaluate_record()` implementation.

This measures a model together with its agent harness and tool/revision budget.
It is not the original one-response SOB leaderboard protocol. Image and audio
splits are not included.

## Data And Evaluation

- `tasks/`: generated Harbor task directories, ready to consume at a Git revision.
  Names use zero-based row numbers (`sob-text-00000` through `sob-text-04999`)
  because upstream record IDs are not unique. All rows and original IDs are retained.
- `convert.py`: deterministic conversion from the pinned test Parquet file.
- `template/`: task environment, verifier wrapper and oracle script.
- `vendor/`: unmodified upstream scoring, prompt and serialization modules with
  their MIT license. Versions and dataset checksum are in `provenance.json`.
- `dataset.toml`: exact sorted task membership for harness-bench's catalog.

The environment is a digest-pinned public Python 3.12 image. No per-task image
build is necessary when Harbor uses `environment.docker_image`. The provided
Dockerfile describes the same image for backends that build environments.
Declared resources: 1 CPU, 2 GiB RAM, 1 GiB writable storage; agent budget 600 s,
verifier budget 180 s. Agent setup and verifier dependency installation need
network access. The verifier installs `jsonschema==4.26.0` in its own venv.

Agent-visible data is in `instruction.md`; reference outputs and scorer inputs
are under `tests/`, which Harbor uploads for verification after the agent stage.
`solution/` contains upstream ground truth for oracle validation.

`reward.json` contains every named upstream metric and `reward`, an alias for
`leaf_value_em` (Truth Score). Other metrics include schema compliance,
faithfulness, path recall, structure coverage, type safety and exact response
match. Missing or malformed answer files are scored as invalid predictions.
Scorer/dependency failures remain infrastructure errors.

The catalog uses unweighted arithmetic means per metric. This is not SOB's
cross-modality composite or schema-complexity-weighted leaderboard score.
The per-record `eval_record.json` preserves difficulty/weight metadata for
separate aggregation. Upstream parsing and scoring are retained, including
their treatment of reference answers that do not satisfy their own schema.

## Reproduce

```bash
uv sync --frozen
uv run --frozen python convert.py --output /tmp/sob-rebuilt/tasks
uv run --frozen python -m unittest test_conversion -v
```

Conversion downloads only the pinned text test file (about 20 MB), verifies its
SHA-256, and requires a fresh output directory. It downloads no task images and
makes no model requests. Tests compare all converted reference answers with the
original evaluator and exercise invalid JSON, schema mismatch and wrong values.

A container oracle run is a separate integration check:

```bash
harbor run --path tasks/<task-name> --agent oracle --n-concurrent 1
```

## License

SOB source and dataset are MIT-licensed. The original source license is preserved
in `vendor/LICENSE`; the dataset license is in `DATASET-LICENSE`. Conversion code
is MIT-licensed; see `LICENSE`.
