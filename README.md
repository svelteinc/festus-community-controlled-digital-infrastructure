# Festus Community-Controlled Digital Infrastructure

This repository contains the planning, governance design, capital structure, and technical implementation for a community-controlled digital infrastructure development in Festus.

## Structure

- `docs/` – narrative, legal, financial, and community-facing documentation.
- `src/` – all application, modeling, and simulation code.
- `configs/` – configuration files and `.template` env files (no secrets).
- `tests/` – unit and integration tests for code in `src/`.
- `scripts/` – short-lived or support scripts (reusable logic should move into `src/common/`).
- `deploy/` – deployment and infrastructure-as-code assets.
- `docker/` – Dockerfiles and container-specific configuration.
- `monitoring/` – logging, metrics, and operational monitoring configs.

## Reuse & Licensing

This project is intended as a public-good playbook that any community can adapt.

- **Code** in `src/` is licensed under the MIT License (see `LICENSE`).
- **Documentation** in `docs/` is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

You are free to copy, modify, and reuse this structure for your own city. Replace “Festus” and FDIA/FCIC naming with your local equivalents, and review all legal/financial documents with qualified counsel before implementation.

## Documentation

See `docs/README.md` for project-specific narrative and design documents.
