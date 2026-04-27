# scitex-plt

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-plt.svg)](https://pypi.org/project/scitex-plt/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-plt.svg)](https://pypi.org/project/scitex-plt/)
[![Tests](https://github.com/ywatanabe1989/scitex-plt/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-plt/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-plt/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-plt/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-plt/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-plt)
[![Docs](https://readthedocs.org/projects/scitex-plt/badge/?version=latest)](https://scitex-plt.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


**SciTeX plotting module** - an alias package for [figrecipe](https://github.com/ywatanabe1989/figrecipe).

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI ⭐⭐ · MCP ⭐⭐⭐ · Skills ⭐⭐ · Hook — · HTTP —

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Matplotlib boilerplate for publication figures** — manually setting DPI, fonts, axis labels, CSV sidecars, and mm-precision layout for every paper figure | **`stx.plt.subplots()`** — thin wrapper around figrecipe returning a tracked axes with `.plot_line(...)`, `set_xyt(...)`, and publication-ready defaults |
| 2 | **Figure and underlying data drift apart** — the PNG lives in the repo, the CSV that generated it sits in a notebook cell and eventually disappears | **Auto CSV export on save** — `stx.io.save(fig, "plot.png")` writes `plot.png` + `plot.csv` + `plot.yaml` atomically so the data is always reproducible |
| 3 | **No way for AI agents to generate figures** — coding agents need a structured API, not matplotlib's stateful pyplot | **MCP tools (`plt_line`, `plt_scatter`, `plt_stx_*`)** — agents compose publication plots from CSVs via column specs, no inline arrays needed |

## Installation

```bash
pip install scitex-plt
```

This will automatically install `figrecipe` as a dependency.

## Usage

```python
import scitex_plt as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.save(fig, "figure.png")
```

## About

`scitex-plt` is part of the [SciTeX](https://scitex.ai) ecosystem. It provides
the same API as `figrecipe` for users who prefer the `scitex-plt` package name.

For full documentation, see [figrecipe](https://github.com/ywatanabe1989/figrecipe).

## License

AGPL-3.0 - same as figrecipe.
