---
description: |
  [TOPIC] CLI reference
  [DETAILS] `scitex-plt` console entry — figrecipe CLI under the scitex-* name. plot, reproduce, compose, crop, diagram, style.
tags: [scitex-plt-cli-reference]
---

# CLI Reference

```
scitex-plt [OPTIONS] COMMAND [ARGS]...
```

`scitex-plt` is the same console entry as `figrecipe` — the `[project.scripts]`
table maps `scitex-plt = "figrecipe._cli:main"`. Every flag and command
is identical between the two binaries.

## Global options

| Flag | Purpose |
|---|---|
| `-V`, `--version` | Show version and exit |
| `--help-recursive` | Show help for all commands |
| `--json` | Emit structured JSON (propagates to subcommands) |
| `-h`, `--help` | Show this message and exit |

## Configuration precedence

```
config.yaml -> $FIGRECIPE_CONFIG -> ~/.scitex/figrecipe/config.yaml -> defaults
```

## Commands

### Figure creation

| Command | Purpose |
|---|---|
| `plot` | Create a figure from a declarative YAML/JSON spec |
| `reproduce` | Reproduce a figure from a YAML recipe |
| `compose` | Compose multiple figures into one |
| `gui` | Launch interactive GUI editor |

### Image processing

| Command | Purpose |
|---|---|
| `convert` | Convert between figure formats |
| `crop` | Crop an image to its content area |
| `diff` | Compare two images and report pixel differences |
| `hitmap` | Generate hitmap visualization from two images |

### Data + validation

| Command | Purpose |
|---|---|
| `extract` | Extract plotted data arrays from a recipe |
| `validate` | Validate that a recipe reproduces its original figure |
| `info` | Show information about a recipe |

### Diagram + style

| Command | Purpose |
|---|---|
| `diagram` | Create and manage diagrams (flowcharts, pipelines, …) |
| `style` | Manage figure styles and presets |
| `fonts` | List or check available fonts |

## Examples

```bash
scitex-plt plot recipe.yaml
scitex-plt reproduce figure.png.recipe.yaml
scitex-plt crop figure.png
scitex-plt diagram --help
```

For per-command flags, run `scitex-plt <command> --help` or
`scitex-plt --help-recursive`.

## See also

- **figrecipe** `_skills/figrecipe/11_cli-reference.md` — same surface, fuller examples
