---
description: |
  [TOPIC] Python API
  [DETAILS] All public callables — re-exports from figrecipe (subplots, save, reproduce, compose, crop, …).
tags: [scitex-plt-python-api]
---

# Python API

```python
import scitex_plt as plt
```

Because `scitex_plt is figrecipe`, the public surface is identical.

## Plotting

| Symbol | Purpose |
|---|---|
| `subplots(...)` | Drop-in `matplotlib.pyplot.subplots` returning enriched `Figz` / `Pltz` |
| `Figz`, `Pltz` | Enriched figure / axes wrappers |
| `sns` | Seaborn passthrough (with style harmonization) |

## Save / load / reproduce

| Symbol | Purpose |
|---|---|
| `save(fig, path)` | Save image + companion CSV |
| `load(path)` | Load a saved figure spec |
| `reproduce(spec)` | Re-render from a recipe |
| `save_bundle(...)`, `load_bundle(...)`, `reproduce_bundle(...)` | ZIP bundle (spec + data + exports) |

## Layout / composition

| Symbol | Purpose |
|---|---|
| `compose(...)` | Multi-panel composition |
| `align_panels(...)`, `distribute_panels(...)`, `align_smart(...)` | Panel layout helpers |
| `crop(img, ...)` | Whitespace-aware image cropping |

## Styles + diagrams

| Symbol | Purpose |
|---|---|
| `load_style(name)`, `unload_style()`, `list_presets()` | SCITEX / MATPLOTLIB presets |
| `colors`, `signature`, `caption_with_signature` | Palette + provenance helpers |
| `Diagram` | Box-and-arrow diagrams (Mermaid / Graphviz) |

## Inspect / validate / extract

| Symbol | Purpose |
|---|---|
| `info(spec)`, `validate(spec)`, `extract_data(spec)` | Recipe introspection |
| `gui()` | Launch interactive editor |

## See also

- **figrecipe** `_skills/figrecipe/` — authoritative deep-dives
- `scitex-io` — `stx.io.save(fig, ...)` is the canonical entry-point
