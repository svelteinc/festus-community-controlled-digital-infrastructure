"""Run a Phase 1 capital stack scenario from environment variables.

This is a small CLI helper that lets you exercise the Phase 1 capital stack
model without opening a notebook. It is intentionally simple and suitable for
local exploration only.

Defaults mirror the baseline example in
`docs/capital_stack/phase1_capital_stack_example_v1.md`. You can override
values with environment variables, for example:

    CCDI_TOTAL_PROJECT_COST=120000000 \
    CCDI_SENIOR_DEBT_RATIO=0.55 \
    CCDI_CAPACITY_MW=25 \
    python scripts/run_capital_stack_scenario.py

The script assumes you have activated an environment where those variables are
set (for example by exporting them or using your own `.env` loader).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dataclasses import dataclass

# Ensure the repository root is on sys.path so `src/` imports work when this
# script is executed directly (e.g. `python scripts/run_capital_stack_scenario.py`).
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.simulator.capital_stack import (  # noqa: E402
    Phase1CapitalStackInputs,
    compute_phase1_capital_stack,
)


def _env_float(name: str, default: float) -> float:
    """Return a float from the environment or a default.

    Raises SystemExit with a helpful message if the value cannot be parsed.
    """

    value = os.getenv(name)
    if value is None:
        return default

    try:
        return float(value)
    except ValueError as exc:  # pragma: no cover - trivial I/O branch
        raise SystemExit(f"Invalid value for {name}: {value!r}, expected a number") from exc


def main() -> None:
    """Compute and print a simple Phase 1 capital stack scenario."""

    inputs = Phase1CapitalStackInputs(
        total_project_cost=_env_float("CCDI_TOTAL_PROJECT_COST", 100_000_000.0),
        senior_debt_ratio=_env_float("CCDI_SENIOR_DEBT_RATIO", 0.6),
        annual_interest_rate=_env_float("CCDI_ANNUAL_INTEREST_RATE", 0.06),
        debt_tenor_years=int(_env_float("CCDI_DEBT_TENOR_YEARS", 15.0)),
        annual_cash_flow_available_for_debt_service=_env_float(
            "CCDI_CFADS", 15_000_000.0
        ),
        capacity_mw=_env_float("CCDI_CAPACITY_MW", 20.0),
        ground_rent_per_mw=_env_float("CCDI_GROUND_RENT_PER_MW", 50_000.0),
        usage_fee_per_mw=_env_float("CCDI_USAGE_FEE_PER_MW", 10_000.0),
    )

    outputs = compute_phase1_capital_stack(inputs)

    print("Phase 1 capital stack scenario")
    print("-" * 40)
    print(f"Total project cost:          ${inputs.total_project_cost:,.0f}")
    print(f"Senior debt ratio:           {inputs.senior_debt_ratio:.2f}")
    print(f"Senior debt amount:          ${outputs.senior_debt_amount:,.0f}")
    print(f"Equity amount:               ${outputs.equity_amount:,.0f}")
    print("")
    print(f"Annual interest rate:        {inputs.annual_interest_rate:.2%}")
    print(f"Debt tenor (years):          {inputs.debt_tenor_years}")
    print(f"Annual debt service:         ${outputs.annual_debt_service:,.0f}")
    print(
        f"CFADS (before community):    ${inputs.annual_cash_flow_available_for_debt_service:,.0f}"
    )
    print(f"Debt service coverage ratio: {outputs.debt_service_coverage_ratio:.2f}")
    print("")
    if inputs.capacity_mw is not None:
        print(f"Capacity:                    {inputs.capacity_mw:.1f} MW")
    print(f"Annual community revenue:    ${outputs.annual_community_revenue:,.0f}")


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()

