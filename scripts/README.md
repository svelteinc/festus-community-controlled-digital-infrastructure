# Scripts

This directory contains small helper scripts for running CCDI-related analyses.

## Available scripts

- `run_capital_stack_scenario.py`
  - Runs a baseline Phase 1 capital stack scenario using the assumptions described in
    `docs/capital_stack/phase1_capital_stack_v1.md`.
  - Useful for City Managers, finance staff, and advisors who want a quick sense of
    how different capacity, debt, and fee assumptions change DSCR and community revenue.

## How to use (example)

From the repository root:

1. (Optional but recommended) Create and activate a Python virtual environment.
2. Install any required packages listed in project documentation or requirements.
3. Run:
   - `python3 scripts/run_capital_stack_scenario.py`

See `src/simulator/capital_stack.py` and `src/simulator/sensitivity.py` if you
want to extend or customize the modeling in code.

