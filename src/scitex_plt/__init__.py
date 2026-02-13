"""scitex-plt - SciTeX plotting module (alias for figrecipe).

This package is a thin wrapper that re-exports figrecipe's public API.
Install with: pip install scitex-plt

Usage
-----
>>> import scitex_plt as plt
>>> fig, ax = plt.subplots()
>>> ax.plot([1, 2, 3], [1, 4, 9])
>>> plt.save(fig, "figure.png")
"""

from figrecipe import *  # noqa: F401,F403
from figrecipe import __all__ as _fr_all
from figrecipe import __version__

__all__ = list(_fr_all) + ["__version__"]
