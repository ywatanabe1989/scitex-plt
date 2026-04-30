"""Smoke tests for scitex_plt package.

Minimal checks that the public API imports cleanly and basic
plotting helpers can be invoked without raising. These are not
exhaustive tests; they exist so CI has something to run.
"""

from __future__ import annotations

import importlib

import pytest


def test_import_scitex_plt():
    """Top-level package imports."""
    mod = importlib.import_module("scitex_plt")
    assert mod is not None


@pytest.mark.parametrize(
    "name",
    [
        "subplots",
        "save",
        "load",
        "compose",
        "crop",
        "extract_data",
        "reproduce",
        "validate",
        "colors",
        "signature",
    ],
)
def test_public_api_exposes(name):
    """Documented public-API symbols are accessible from the top namespace."""
    import scitex_plt

    assert hasattr(scitex_plt, name), f"scitex_plt missing public symbol: {name}"


def test_subplots_returns_fig_axes():
    """scitex_plt.subplots returns a matplotlib-like (fig, ax) pair."""
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    import scitex_plt

    fig, ax = scitex_plt.subplots()
    assert fig is not None
    assert ax is not None


def test_list_presets_runs():
    """Preset listing helpers don't blow up on empty / default state."""
    import scitex_plt

    # Both helpers exist; calling them should not raise.
    scitex_plt.list_presets()
    scitex_plt.list_graph_presets()


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])
