# Source Code

All application, modeling, and simulation code for the Festus CCDI project lives under `src/`.

Planned subpackages:
- `common/` – shared utilities (config loading, logging, data models).
- `agents/` – simulation/decision agents (city, operator, community, lenders).
- `data_pipeline/` – ingestion and transformation of external data.
- `orchestrator/` – coordination of workflows and scenario runs.
- `simulator/` – simulation engines and analytical models.


## Developer quickstart

1. Create and activate a virtual environment (example):
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
2. Install any required packages listed in project docs or requirements (if present).
3. Run unit tests (once dependencies are installed):
   - `pytest`
4. Run the baseline capital stack scenario:
   - `python3 scripts/run_capital_stack_scenario.py`

Use `src/simulator/capital_stack.py` and `src/simulator/sensitivity.py` as starting points if you want to extend the financial modeling.
