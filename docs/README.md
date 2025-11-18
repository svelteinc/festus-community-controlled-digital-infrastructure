# Festus CCDI Documentation

This directory contains the conceptual, legal, financial, and community-facing documentation for the Festus Community-Controlled Digital Infrastructure (CCDI) program.

## Subdirectories

- `vision/` – goals, principles, and high-level narrative.
- `governance/` – FDIA/FCIC structure, board seats, bylaws, decision rules, and the city-wide FCIIA/FCA civic authority + assembly concept.
- `capital_stack/` – financing models, term sheets, and risk analyses.
- `rfp/` – RFP drafts, evaluation criteria, and operator covenant templates.
- `community_engagement/` – public-facing materials, FAQs, and feedback logs.
- `tokenization/` – Phase 2+ tokenized community bond/RWA designs.

Each subdirectory should contain focused markdown documents instead of large monolithic files.
## How to Use This Repo

- **If you are in Festus:** start with `vision/project_vision_v1.md` and `vision/festus_council_briefing_v1.md` to align on goals, then review `governance/FDIA_FCIC_governance_v1.md` and `capital_stack/phase1_capital_stack_v1.md` before sharing the FAQ and Facebook explainer from `community_engagement/`. If you want to see how this can evolve into a city-wide Civic Authority & Assembly, also read `governance/festus_citywide_civic_authority_and_assembly_v1.md`.
- **If you are another community:** read `docs/adaptation_guide_for_other_communities.md` first, then copy this structure and swap in your own authority names, governance parameters, and financing assumptions.
- **If you are a developer or analyst:** use `docs/` to understand the political/financial intent, then look at `src/` and `tests/` for code and models that implement or stress-test these designs.
- **For quick numeric intuition:** see `capital_stack/phase1_capital_stack_example_v1.md` and the CLI helper in `scripts/run_capital_stack_scenario.py`. For more advanced sweeps, check `src/simulator/sensitivity.py` for simple DSCR and leverage sensitivity helpers.


## How to Adapt for Other Communities

This documentation is written for Festus, but other cities can reuse it by:
- Replacing “Festus” and FDIA/FCIC with your local authority names.
- Adjusting governance details to match your legal and political context.
- Updating financial assumptions and covenants to reflect local realities.

## Documentation License

The documentation in `docs/` is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to share and adapt these materials, provided you give appropriate credit and indicate if changes were made.


## Community Standards & Security

Contributions to this documentation and the associated code are governed by the
project Code of Conduct (`CODE_OF_CONDUCT.md`). Security issues should be
reported privately as described in `SECURITY.md` rather than opened as public
issues.
