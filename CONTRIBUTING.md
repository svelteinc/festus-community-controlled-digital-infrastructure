# Contributing to the Festus CCDI Playbook

Thank you for your interest in improving this public-good project. This
repository is meant to be **reusable by other communities**, so contributions
should keep things clear, conservative, and easy to adapt.

## Code of Conduct

Be respectful. Assume good faith. This project is about helping communities
make better decisions, not winning arguments.

## How to Contribute

- **Questions / ideas:** Open an issue describing the context (Festus or another
  community) and what you are trying to achieve.
- **Bug fixes / small improvements:** Open a pull request with a concise
  description and reference any related issues.
- **Larger proposals:** Start with an issue or brief design document so others
  can comment before you invest a lot of time.

## Coding Guidelines

- **Language:** Python for code under `src/`.
- **Style:** Follow PEP 8 (4-space indents, meaningful names). Use absolute
  imports from `src/...`.
- **Tests:** Add or update tests under `tests/` for any behavior change. Aim for
  good coverage on core modules (especially `src/common/`, agents, and
  simulators).
- **Configuration:** New configuration values should flow through
  `src/common/config.py` and be documented in `configs/.env.template`.
- **Logging:** Use the shared logger from `src/common/logging.py`. Avoid
  printing directly to stdout in library code.

## Documentation Guidelines

- Place new conceptual or public-facing docs under `docs/` in the appropriate
  subdirectory.
- Include a short **TL;DR** near the top of longer documents in plain English.
- For financial or legal content, include a **clear disclaimer** indicating that
  it is a conceptual example and not legal, tax, or investment advice.
- When adding Festus-specific details, consider whether they should also be
  parameterized so other communities can adapt them.

## Licensing

- **Code** contributions are accepted under the MIT License.
- **Documentation** contributions are accepted under the Creative Commons
  Attribution 4.0 International License (CC BY 4.0).

By submitting a pull request, you agree that your contributions will be
licensed under these terms so that other communities can freely reuse and
adapt this work.

