# Phase 1 Capital Stack Example (Jupyter-Friendly)

> **Note:** This is a conceptual example for discussion only and is not legal,
> tax, or investment advice.

This example shows how to use the `src/simulator/capital_stack.py` helper in a
Python REPL or Jupyter notebook to explore a simple Phase 1 scenario.

## 1. Scenario 1 – Festus-style baseline

- 20 MW initial facility.
- Total project cost: $100M.
- Senior debt: 60% of total cost at 6% over 15 years.
- CFADS (cash flow available for debt service): $15M per year.
- Community revenues:
  - Ground rent: $50,000/MW/year.
  - Usage fee: $10,000/MW/year.

## 2. Scenario 2 – Regional hub comparison

- 80 MW facility.
- Total project cost: $200M.
- Senior debt: 65% of total cost at 6.5% over 20 years.
- CFADS: $30M per year.
- Community revenues:
  - Ground rent: $40,000/MW/year.
  - Usage fee: $15,000/MW/year.

This lets you see how scaling capacity and adjusting leverage and fees changes
DSCR, equity requirements, and community revenues.

## 3. Example code (baseline)

In a Jupyter notebook cell:

```python
from src.simulator.capital_stack import (
    Phase1CapitalStackInputs,
    compute_phase1_capital_stack,
)

inputs = Phase1CapitalStackInputs(
    total_project_cost=100_000_000.0,
    senior_debt_ratio=0.6,
    annual_interest_rate=0.06,
    debt_tenor_years=15,
    annual_cash_flow_available_for_debt_service=15_000_000.0,
    # Work in MW as well as dollars
    capacity_mw=20.0,
    ground_rent_per_mw=50_000.0,
    usage_fee_per_mw=10_000.0,
)

outputs = compute_phase1_capital_stack(inputs)
outputs
```

## 4. Example code (regional hub)

In a separate cell, you can paste this and tweak further:

```python
regional_inputs = Phase1CapitalStackInputs(
    total_project_cost=200_000_000.0,
    senior_debt_ratio=0.65,
    annual_interest_rate=0.065,
    debt_tenor_years=20,
    annual_cash_flow_available_for_debt_service=30_000_000.0,
    capacity_mw=80.0,
    ground_rent_per_mw=40_000.0,
    usage_fee_per_mw=15_000.0,
)

regional_outputs = compute_phase1_capital_stack(regional_inputs)
regional_outputs
```

Inspecting `outputs` and `regional_outputs` will show:

- `senior_debt_amount`
- `equity_amount`
- `annual_debt_service`
- `debt_service_coverage_ratio` (DSCR)
- `annual_community_revenue` (derived from MW-based fees in these examples)

## 5. Next steps

You can copy either cell and tweak:

- `capacity_mw`
- `senior_debt_ratio`
- `annual_interest_rate` and `debt_tenor_years`
- `ground_rent_per_mw` and `usage_fee_per_mw`

This lets you quickly explore how different assumptions affect DSCR and
community revenues before building a more detailed financial model.

