"""scitex-plt — sys.modules alias for figrecipe.

scitex-plt is a thin namespace alias that makes `import scitex_plt` resolve
to the figrecipe package. Identity-equal: `scitex_plt is figrecipe` → True.
This matches the alias pattern used elsewhere in the SciTeX ecosystem
(e.g. `scitex.gen` is `scitex_gen`).

Install with: `pip install scitex-plt`

Usage
-----
>>> import scitex_plt as plt
>>> fig, ax = plt.subplots()
>>> ax.plot([1, 2, 3], [1, 4, 9])
>>> plt.save(fig, "figure.png")
"""

from __future__ import annotations

import sys as _sys

try:
    import figrecipe as _real
except ImportError as _e:
    raise ImportError(
        "scitex-plt requires the 'figrecipe' package. "
        "Install with: pip install figrecipe  (or: pip install scitex-plt)"
    ) from _e

_sys.modules[__name__] = _real

# This module replaces itself in sys.modules with figrecipe (above).
# `__all__` is declared for tooling (auditors, IDE introspection) — the
# actual exports come from figrecipe after the swap.
__all__: list[str] = []
