"""Smoke test for examples/01_basic.py.

Per scitex-dev audit-project PS303: every example must have a matching
test under tests/examples/. Validates the example parses cleanly and
that its `main()` entry point returns the documented zero-exit status.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path


EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "01_basic.py"


def test_basic_example_file_exists_on_disk():
    # Arrange
    expected_path = EXAMPLE

    # Act
    found = expected_path.exists()

    # Assert
    assert found is True, f"missing example file: {expected_path}"


def test_basic_example_compiles_with_py_compile():
    # Arrange
    cmd = [sys.executable, "-m", "py_compile", str(EXAMPLE)]

    # Act
    completed = subprocess.run(cmd, capture_output=True, text=True)

    # Assert
    assert completed.returncode == 0, completed.stderr


def test_basic_example_main_returns_zero_exit_status():
    # Arrange
    spec = importlib.util.spec_from_file_location("scitex_plt_example_01", EXAMPLE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Act
    exit_status = module.main()

    # Assert
    assert exit_status == 0
