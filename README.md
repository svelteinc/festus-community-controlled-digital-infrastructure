# Festus Community-Controlled Digital Infrastructure

Public-good playbook for a community-controlled digital infrastructure platform in Festus, MO: governance, capital stack, and engagement model that any city can adapt.

This repository contains a practical, reusable playbook for structuring a community-controlled digital infrastructure project (e.g., data center) in Festus, Missouri. It includes:

- A governance model (FDIA/FCIC) that keeps land and covenants in local hands.
- A conservative Phase 1 capital stack that uses private debt/equity while protecting the city's budget.
- A city-wide civic authority and resident assembly concept (FCIIA/FCA) that extends this model beyond a single project.
- Optional Phase 2 tokenization concepts for community bonds.
- Public-facing materials (vision, council briefing, Facebook explainer, FAQ) that other communities can adapt.
- Code is licensed under MIT, documentation under CC BY 4.0, so any city can clone, adapt, and improve this model.

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

## Who you are / where to start

- **City leaders / City Manager / EDC staff:**
  - `docs/vision/festus_city_manager_implementation_roadmap_v1.md`
  - `docs/vision/project_vision_v1.md`
  - `docs/vision/festus_council_briefing_v1.md`
  - `docs/vision/festus_desoto_corridor_strategy_v1.md`
  - `docs/vision/festus_corridor_state_edc_brief_v1.md`

- **Residents / civic volunteers:**
  - `docs/community_engagement/faq_v1.md`
  - `docs/community_engagement/festus_facebook_explainer_v1.md`
  - `docs/community_engagement/festus_dc_options_onepager_v1.md`
  - `docs/community_engagement/data_center_numbers_onepager_v1.md`

- **Lawyers / finance / advisors:**
  - `docs/governance/FDIA_FCIC_governance_v1.md`
  - `docs/governance/festus_dc_zoning_model_v1.md`
  - `docs/governance/festus_dc_sample_ordinance_clauses_v1.md`
  - `docs/capital_stack/phase1_capital_stack_v1.md`
  - `docs/capital_stack/festus_cfo_deal_evaluation_cheatsheet_v1.md`
  - `docs/rfp/operator_rfp_skeleton_v1.md`
  - `docs/tokenization/tokenized_community_bonds_v1.md`

- **Developers / analysts:**
  - `src/README.md`
  - `tests/README.md`
  - `scripts/run_capital_stack_scenario.py`
  - `src/simulator/capital_stack.py`
  - `src/simulator/sensitivity.py`


## Quick Start for Cities

If you want to "see the numbers" quickly:

1. Clone this repository.
2. Run the baseline Phase 1 scenario from your shell:
   - `python3 scripts/run_capital_stack_scenario.py`
3. For notebook-based exploration, open
   `docs/capital_stack/phase1_capital_stack_example_v1.md` and copy the example
   cells into a Jupyter notebook. Adjust capacity (MW), debt ratio, interest
   rate, and community fee assumptions to see how DSCR and community revenues
   move.

These helpers are conceptual and for discussion only; they are not a full
project finance model or investment advice.


## Community Standards & Security

This project follows a Contributor Code of Conduct. By participating, you agree
to uphold it (see `CODE_OF_CONDUCT.md`). For security issues, please do not open
a public GitHub issue; instead, email `gf@svelteinc.co` as described in
`SECURITY.md`. This helps us respond responsibly while keeping the project
public-good and safe for everyone.
