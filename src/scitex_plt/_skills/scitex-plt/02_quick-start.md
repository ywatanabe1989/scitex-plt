---
description: |
  [TOPIC] Quick start
  [DETAILS] Smallest example — subplots → plot_line → save. Same surface as figrecipe.
tags: [scitex-plt-quick-start]
---

# Quick Start

```python
import scitex_plt as plt

fig, ax = plt.subplots()
ax.plot_line([1, 2, 3], [1, 4, 9])
ax.set_xyt("x", "y", "Demo")
plt.save(fig, "figure.png")        # auto-saves figure.png + figure.csv
```

## Why an alias

The ecosystem follows a strict `scitex_<name>` import convention
(`scitex_io`, `scitex_stats`, `scitex_path`, …). `scitex_plt` lets users
keep that naming while figrecipe owns the implementation:

```python
import scitex_plt
import figrecipe
assert scitex_plt is figrecipe   # True — same module object
```

## Save via scitex-io (canonical)

```python
import scitex.io as sio
sio.save(fig, "figure.png")        # writes figure.png + figure.csv
```

## Next

- [03_python-api.md](03_python-api.md) — public surface (= figrecipe's)
- [04_cli-reference.md](04_cli-reference.md) — `scitex-plt` CLI
- **figrecipe's** `_skills/figrecipe/` — full plot catalog, styles, recipes
