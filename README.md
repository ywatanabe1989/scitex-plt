# scitex-plt

**SciTeX plotting module** - an alias package for [figrecipe](https://github.com/ywatanabe1989/figrecipe).

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
