#!/usr/bin/env python3
# File: src/scitex_plt/__main__.py

"""Allow running as: python -m scitex_plt

Delegates to figrecipe's CLI since scitex-plt is a sys.modules alias.
"""

import sys

from figrecipe._cli import main

sys.exit(main())
