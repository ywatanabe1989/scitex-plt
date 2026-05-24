"""Smoke tests for scitex_plt package.

Minimal checks that the public API imports cleanly and basic
plotting helpers can be invoked without raising. These are not
exhaustive tests; they exist so CI has something to run.
"""

from __future__ import annotations

import importlib

import pytest


def test_scitex_plt_top_level_module_imports_cleanly():
    # Arrange
    module_name = "scitex_plt"

    # Act
    mod = importlib.import_module(module_name)

    # Assert
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
def test_public_api_exposes_documented_symbol_at_top_level(name):
    # Arrange
    import scitex_plt

    # Act
    has_symbol = hasattr(scitex_plt, name)

    # Assert
    assert has_symbol is True, f"scitex_plt missing public symbol: {name}"


def test_subplots_returns_figure_with_savefig_attribute():
    # Arrange
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    import scitex_plt

    # Act
    fig, _ax = scitex_plt.subplots()

    # Assert
    assert hasattr(fig, "savefig")


def test_subplots_returns_axes_with_plot_attribute():
    # Arrange
    matplotlib = pytest.importorskip("matplotlib")
    matplotlib.use("Agg")
    import scitex_plt

    # Act
    _fig, ax = scitex_plt.subplots()

    # Assert
    assert hasattr(ax, "plot")


def test_list_presets_returns_list_of_known_preset_names():
    # Arrange
    import scitex_plt

    # Act
    presets = scitex_plt.list_presets()

    # Assert
    assert isinstance(presets, list)


def test_list_graph_presets_returns_mapping_of_preset_descriptions():
    # Arrange
    import scitex_plt

    # Act
    graph_presets = scitex_plt.list_graph_presets()

    # Assert
    assert isinstance(graph_presets, dict)


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])
