# Contributing to scitex-plt

Thanks for your interest in contributing.

## Quick start

1. Fork and clone the repository.
2. Install editable with the dev extras:
   ```bash
   pip install -e ".[dev]"
   ```
3. Run the test suite:
   ```bash
   python -m pytest
   ```
4. Sign the [CLA](CLA.md) when prompted on your first PR.

## Standards

This package follows the SciTeX ecosystem conventions documented under
`scitex_dev._skills.general/` (install `scitex-dev[cli-audit]` and run
`scitex-dev ecosystem audit-all scitex-plt` to verify).

## Pull requests

- One logical change per PR; keep commits focused and the message
  explains the *why*.
- New features need both the API change and the tests/docs update.
- Open an issue first for cross-cutting changes so we can sketch the
  shape together.
