# Festus CCDI – City Manager Implementation Roadmap (Draft v1)

> Working roadmap for a City Manager / CAO / senior staff. Adapt as facts and politics change. Not legal or financial advice.

This roadmap assumes Festus is the first mover, but it is written so other cities can adapt it.

---

## Phase 0 – Get oriented and set the north star

**Goal:** Build a shared mental model inside City Hall of what this project is and is not.

**Read and align on:**
- `docs/vision/project_vision_v1.md` – overall CCDI story and goals.
- `docs/vision/festus_council_briefing_v1.md` – shorter briefing for Mayor/Council.
- `docs/vision/festus_desoto_corridor_strategy_v1.md` – corridor lens: Festus + De Soto + Hematite, "growth with guardrails".

**Decisions:**
- Confirm the high-level **city objectives** (jobs, tax base, risk posture, noise/water/traffic limits, tree/floodplain protection).
- Agree that the corridor will grow under a **clear civic operating system**, not one-off deals.

---

## Phase 1 – Lock in "Growth with Guardrails" policy direction

**Goal:** Make it clear to staff, partners, and investors what types of digital and industrial projects the city wants.

**Key documents:**
- `docs/governance/festus_dc_zoning_model_v1.md` – model for micro/modular vs hyperscale, triggers, and caps.
- `docs/governance/festus_dc_sample_ordinance_clauses_v1.md` – sample legal-style clauses.
- `docs/community_engagement/data_center_numbers_onepager_v1.md` – simple numeric intuition.
- `docs/community_engagement/festus_desoto_corridor_growth_with_guardrails_onepager_v1.md` – resident-facing summary.

**Actions:**
- Ask legal and planning staff to review the **zoning model** and sample clauses and map them onto local code.
- Decide whether to **prohibit or cap** hyperscale data centers in city limits.
- Define preliminary **noise, water, traffic, and tree-cover standards** for any data/digital site.
- Instruct staff that **any new digital infrastructure proposal** must be analyzed against these standards.

---

## Phase 2 – Stand up the civic operating system

**Goal:** Create the entities and rules so residents have a structured say and the city’s balance sheet is protected.

**Key documents:**
- `docs/governance/FDIA_FCIC_governance_v1.md` – project-level authority/corporation.
- `docs/governance/FDIA_FCIC_charter_bylaws_skeleton_v1.md` – articles/bylaws skeleton.
- `docs/governance/festus_citywide_civic_authority_and_assembly_v1.md` – FCIIA/FCA concept.
- `docs/governance/festus_civic_operating_system_explainer_v1.md` – plain-language explainer.

**Actions:**
- With counsel, adapt the **FDIA/FCIC** governance and charter/b ylaws to your legal context.
- Decide when and how to enable a **Festus Civic Infrastructure & Innovation Authority (FCIIA)** and **Festus Civic Assembly (FCA)**:
  - Which decisions are "reserved matters" requiring FCA involvement or supermajority support?
  - How will residents be selected or invited into FCA?
- Draft a clear public explanation of **who decides what** and how residents can intervene.

---

## Phase 3 – Clarify the financial playbook

**Goal:** Know what "good" looks like in dollars before you see a term sheet.

**Key documents and tools:**
- `docs/capital_stack/phase1_capital_stack_v1.md` – baseline capital structure.
- `docs/capital_stack/phase1_capital_stack_example_v1.md` – worked example.
- `docs/tokenization/tokenized_community_bonds_v1.md` – optional community participation layer.
- `scripts/run_capital_stack_scenario.py` – quick CLI scenario runner.
- `src/simulator/capital_stack.py` and `src/simulator/sensitivity.py` – for staff/consultants who want deeper analysis.

**Actions:**
- Have staff or a trusted advisor run a **baseline scenario** using the docs and script.
- Decide your **non-negotiables** before negotiations:
  - Minimum community revenue / fees.
  - Maximum leverage and required DSCR.
  - Whether and how to include **tokenized community bonds** or similar instruments.
- Document these guardrails so they are easy to explain to Council and residents.

---

## Phase 4 – Prepare for partners and RFPs

**Goal:** Signal clearly to potential operators and investors what game they are being invited into.

**Key documents:**
- `docs/rfp/operator_rfp_skeleton_v1.md` – structure for an operator RFP.
- `docs/community_engagement/festus_bitcoin_vs_dc_whos_who_v1.md` – clarifies current players and sites.
- `docs/vision/festus_desoto_corridor_pitch_deck_outline_v1.md` – talking points for regional partners.

**Actions:**
- Customize the **operator RFP skeleton** to your sites and guardrails.
- Use the **corridor pitch deck outline** to brief EDCs, utilities, and state partners.
- Make clear that proposals must:
  - Respect **guardrail zoning and ordinances**.
  - Fit inside an **FDIA/FCIC + FCIIA/FCA** governance structure.
  - Provide transparent financials for modeling.

---

## Phase 5 – Community-facing narrative and engagement

**Goal:** Make sure residents see the whole picture and can shape it, not just react to rumors.

**Key documents:**
- `docs/community_engagement/faq_v1.md` – main FAQ.
- `docs/community_engagement/festus_facebook_explainer_v1.md` – social-ready explainer.
- `docs/community_engagement/festus_dc_options_onepager_v1.md` – options comparison.
- `docs/community_engagement/questions_for_pnz_and_council_v1.md` – structured questions.
- `docs/community_engagement/bitcoin_background_v1.md` and `bitcoin_resident_summary_v1.md` – balanced Bitcoin explainers.
- `docs/community_engagement/community_engagement_plan_v1.md` – overall plan.

**Actions:**
- Decide which documents to treat as **official staff handouts** (with dates, logos, contacts).
- Use the options one-pager and corridor one-pager in **workshops and hearings** so residents see choices.
- Encourage residents to use the PNZ/Council question list and to distinguish **Highway P bitcoin** from the Festus CCDI concept.

---

## Phase 6 – Implementation, monitoring, and iteration

**Goal:** Once a project is live, keep it within guardrails and keep trust.

**Preparation:**
- Define what you will monitor (noise, water use, traffic counts, tree cover, taxes/fees received).
- Decide where monitoring and complaints will be logged and how they will be reported to FCA/Council.

**Actions as projects proceed:**
- Require regular **operator reporting** into FDIA/FCIC and FCIIA.
- Schedule **periodic FCA reviews** of big projects and any proposed expansions.
- Use findings to tighten ordinances, update the capital playbook, and adjust the corridor strategy.

---

## How to adapt this roadmap for your city

- Swap in your own authority names and legal references.
- Adjust corridor geography and anchor projects to match your reality.
- Calibrate financial and environmental guardrails to your risk tolerance.
- Keep the **structure** – vision → guardrails → entities → finance → RFPs → engagement → monitoring – so residents and partners can follow the story.

