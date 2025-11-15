# Phase 1 Capital Stack Example (Jupyter-Friendly)

> **Note:** This is a conceptual example for discussion only and is not legal,
> tax, or investment advice.

This example shows how to use the `src/simulator/capital_stack.py` helper in a
Python REPL or Jupyter notebook to explore a simple Phase 1 scenario.

## 1. Scenario

- 20 MW initial facility.
- Total project cost: $100M.
- Senior debt: 60% of total cost at 6% over 15 years.
- CFADS (cash flow available for debt service): $15M per year.
- Community revenues:
  - Ground rent: $50,000/MW/year.
  - Usage fee: $10,000/MW/year.

## 2. Example code

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

Inspecting `outputs` will show:

- `senior_debt_amount`
- `equity_amount`
- `annual_debt_service`
- `debt_service_coverage_ratio` (DSCR)
- `annual_community_revenue` (derived from MW-based fees in this example)

## 3. Next steps

You can copy this cell and tweak:

- `capacity_mw`
- `senior_debt_ratio`
- `annual_interest_rate` and `debt_tenor_years`
- `ground_rent_per_mw` and `usage_fee_per_mw`

This lets you quickly explore how different assumptions affect DSCR and
community revenues before building a more detailed financial model.

