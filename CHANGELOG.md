# Changelog

All notable changes to `scitex-plt` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.24.7]

### Fixed
- Bumped the `figrecipe` dependency floor `>=0.24.0` → `>=0.30.0`. figrecipe
  0.30.0 is the first release carrying the `gui` command GROUP (`open`/
  `serve`/`status`/`stop`) that `scitex-plt gui serve` requires — a fresh
  install on the old floor could still resolve an older figrecipe lacking
  the group entirely, breaking `scitex-plt gui serve` at runtime
  (`'serve'` was read as a positional SOURCE path, not a subcommand).

## [0.24.4]

- Initial CHANGELOG entry — see git log for prior history.
