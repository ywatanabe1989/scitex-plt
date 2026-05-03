---
name: scitex-plt
description: |
  [WHAT] Thin namespace alias.
  [WHEN] Use when you want the figrecipe API but prefer the `scitex_*` import naming for consistency across the ecosystem (`scitex_io`, `scitex_stats`, `scitex_plt`).
  [HOW] `import scitex_plt` then call `plt.subplots()`.
tags: [scitex-plt]
allowed-tools: mcp__scitex__plt_*
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 2
  hook: 0
  http: 0
canonical-location: scitex-plt/src/scitex_plt/_skills/scitex-plt/SKILL.md
---


> **Interfaces:** Python ⭐⭐⭐ (primary, via figrecipe) · CLI — · MCP — · Skills ⭐⭐ · Hook — · HTTP —

# scitex-plt

`scitex_plt` is a `sys.modules` alias for `figrecipe`. They are
identity-equal:

```python
import scitex_plt
import figrecipe
assert scitex_plt is figrecipe   # True
```

## Why an alias

The ecosystem follows a strict `scitex_<name>` import convention
(`scitex_io`, `scitex_stats`, `scitex_path`, …) that user code latches
onto. Plotting is provided by figrecipe, which keeps a non-prefixed
PyPI name for discoverability. The alias lets users keep the `scitex_*`
naming without a real second package:

```python
import scitex_plt as plt
fig, ax = plt.subplots()
ax.plot_line([1, 2, 3], [1, 4, 9])
ax.set_xyt("x", "y", "Demo")
plt.save(fig, "figure.png")        # auto-saves figure.png + figure.csv
```

## Install

```bash
pip install scitex-plt   # pulls figrecipe automatically
```

If figrecipe is missing at import time, `scitex-plt` raises an explicit
`ImportError` pointing the user at `pip install figrecipe`.

## Where the real docs live

All API, plot-type catalog, paper modes, MCP tools — all in
**figrecipe's** SKILL.md. This file exists so agents searching for "how
do I plot in scitex" find the alias and know where to look.

## See also

- `figrecipe` — the actual implementation
- `scitex-io` — `stx.io.save(fig, ...)` is the canonical figure save
  entry-point and writes the companion CSV automatically
