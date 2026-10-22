#!/bin/bash
set -euo pipefail

python3 -m venv /tmp/sob-verifier
/tmp/sob-verifier/bin/pip install --disable-pip-version-check --quiet jsonschema==4.26.0
/tmp/sob-verifier/bin/python /tests/verify.py
