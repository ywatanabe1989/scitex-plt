"""Pytest fixtures and rootdir marker for this package.

A conftest.py at tests/ is the canonical SciTeX convention
(audit-project PS208) — it pins the pytest rootdir and gives
downstream fixtures a home.

Additionally wires up subprocess coverage so that any child
Python interpreter (subprocess.run, jupyter nbconvert --execute,
``python -m scitex_plt``) emits a coverage shard that
``coverage combine`` picks up. See skill leaf
``05_development_06_subprocess-coverage.md`` for the rationale —
in short: force-set (NOT setdefault) ``COVERAGE_PROCESS_START``
and ``COVERAGE_FILE`` at conftest import time, and drop an
idempotent ``.pth`` shim into site-packages.
"""

from __future__ import annotations

import os
import sysconfig
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
os.environ["COVERAGE_PROCESS_START"] = str(_PROJECT_ROOT / "pyproject.toml")
os.environ["COVERAGE_FILE"] = str(_PROJECT_ROOT / ".coverage")


def _ensure_subprocess_coverage_shim() -> None:
    """Install (idempotently) a .pth shim that boots coverage in children."""
    purelib = Path(sysconfig.get_paths()["purelib"])
    pth = purelib / "_scitex_plt_subprocess_coverage.pth"
    shim = (
        "import os, coverage\n"
        "if os.environ.get('COVERAGE_PROCESS_START'):\n"
        "    coverage.process_startup()\n"
    )
    try:
        if not pth.exists() or pth.read_text() != shim:
            pth.write_text(shim)
    except OSError:
        # Read-only system Python / permission issue — skip silently.
        pass


_ensure_subprocess_coverage_shim()
