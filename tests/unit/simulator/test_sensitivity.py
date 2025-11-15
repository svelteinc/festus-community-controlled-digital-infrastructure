from __future__ import annotations

from typing import List

from src.simulator.capital_stack import Phase1CapitalStackInputs
from src.simulator.sensitivity import sweep_interest_rate, sweep_senior_debt_ratio


def _baseline_inputs() -> Phase1CapitalStackInputs:
    """Return a baseline set of inputs for sensitivity tests."""

    return Phase1CapitalStackInputs(
        total_project_cost=100_000_000.0,
        senior_debt_ratio=0.6,
        annual_interest_rate=0.06,
        debt_tenor_years=15,
        annual_cash_flow_available_for_debt_service=15_000_000.0,
        capacity_mw=20.0,
        ground_rent_per_mw=50_000.0,
        usage_fee_per_mw=10_000.0,
    )


def test_sweep_interest_rate_dscr_is_monotonic() -> None:
    base = _baseline_inputs()
    rates = [0.04, 0.06, 0.08]

    outputs = sweep_interest_rate(base, rates)

    assert len(outputs) == len(rates)
    dscr_values: List[float] = [o.debt_service_coverage_ratio for o in outputs]

    # Higher interest rates should reduce DSCR when everything else is fixed.
    assert dscr_values[0] > dscr_values[1] > dscr_values[2]


def test_sweep_senior_debt_ratio_dscr_is_monotonic() -> None:
    base = _baseline_inputs()
    debt_ratios = [0.4, 0.6, 0.7]

    outputs = sweep_senior_debt_ratio(base, debt_ratios)

    assert len(outputs) == len(debt_ratios)
    dscr_values: List[float] = [o.debt_service_coverage_ratio for o in outputs]

    # More leverage (higher debt ratio) should reduce DSCR, all else equal.
    assert dscr_values[0] > dscr_values[1] > dscr_values[2]

