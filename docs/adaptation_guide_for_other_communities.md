# Adapting the Festus CCDI Playbook for Other Communities (Draft v1)

This guide explains how other cities, towns, and regions can adapt the Festus Community-Controlled Digital Infrastructure (CCDI) playbook.

It is **not legal, tax, or investment advice**. Any real project must be designed and implemented with qualified local legal and financial advisors.

---

## 1. Rename and Re-scope

1. Replace "Festus" with your own community name across documentation.
2. Replace FDIA/FCIC with your own public entity or authority name (e.g., "Springfield Digital Infrastructure Authority").
3. Confirm that your jurisdiction allows a similar public entity structure (authority, corporation, district, etc.).

---

## 2. Governance Parameters to Tune

Use `docs/governance/FDIA_FCIC_governance_v1.md` as a project-level template, and (optionally) `docs/governance/festus_citywide_civic_authority_and_assembly_v1.md` as an example of how a city-wide civic authority and resident assembly could work. Adjust:

- **Board size and composition**
  - Number of seats.
  - Mix of city appointees, institutions, citizens, and experts.
- **Term lengths and limits**
  - Length of terms (e.g., 3 or 4 years).
  - Maximum consecutive terms.
- **Reserved matters and vetoes**
  - Which decisions require supermajority vs. simple majority.
  - When citizen representatives must support a decision.
- **Committee structure**
  - Audit/finance, community/environment, technical/infra committees.
  - Required citizen representation on each committee.

All governance choices should be checked against local law and charter/ordinance requirements.

---

## 3. Capital Stack Parameters to Tune

Use `docs/capital_stack/phase1_capital_stack_v1.md` as a conceptual template, but adapt:

- **Project scale**
  - Order-of-magnitude cost and size.
- **Debt vs. equity mix**
  - Target leverage (e.g., 50–65% senior debt, 35–50% equity) based on lender appetite.
- **Ground rent and fee formulas**
  - Fixed ground rent per MW or per facility.
  - Variable fee structure (e.g., per-MW or revenue-based).
- **Community bond options**
  - Whether local law permits revenue bonds or similar instruments.
  - Who may buy them (residents, institutions, broader investors).

All financial structures must be vetted with local legal and financial advisors and aligned with applicable securities laws.

---

## 4. Community Engagement and Narrative

Adapt `docs/community_engagement/` and `docs/vision/` to local context:

- Tailor examples and language to local concerns (noise, water, traffic, jobs).
- Identify local groups and channels (Facebook groups, neighborhood associations, local press).
- Translate key materials if your community uses multiple languages.

The goal is to **share early, listen carefully, and revise** before any binding decisions.

---

## 5. Legal and Financial Review

Before moving beyond discussion:

1. Engage local counsel to convert the governance outline into a formal charter/bylaws.
2. Work with financial advisors to draft term sheets and bond documents consistent with local rules.
3. Stress-test the capital stack and covenant structure for downside scenarios.

---

## 6. Licensing Reminder

- **Documentation** (`docs/`) is licensed under **CC BY 4.0** – you may copy, adapt, and reuse with attribution.
- **Code** (`src/`) is licensed under **MIT** – you may reuse and modify, with the copyright and license notice preserved.

If you publish your adapted version, consider keeping a similar public-good licensing approach so other communities can benefit as well.



## 7. Land Use & Zoning Considerations

Many communities will also need to tune **where and how** data centers and edge sites are allowed.

As a starting point, see `docs/governance/festus_dc_zoning_model_v1.md` for a conceptual zoning model that:

- Prohibits hyperscale data centers in city limits by default.
- Allows micro/modular and edge sites in appropriate industrial/utility districts with tight performance standards.
- Ties larger compute uses to resident approval via a civic assembly when they cross defined thresholds.

Your local counsel and planning staff should translate those ideas into your own zoning districts and comprehensive plan.


For examples of how these concepts translate into legal-style drafting, see also `docs/governance/festus_dc_sample_ordinance_clauses_v1.md`.
