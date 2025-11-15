import pytest

from src.simulator.capital_stack import (
    Phase1CapitalStackInputs,
    compute_phase1_capital_stack,
)


def test_compute_phase1_capital_stack_basic_scenario() -> None:
    inputs = Phase1CapitalStackInputs(
        total_project_cost=100_000_000.0,
        senior_debt_ratio=0.6,
        annual_interest_rate=0.06,
        debt_tenor_years=15,
        annual_cash_flow_available_for_debt_service=15_000_000.0,
        annual_ground_rent=1_000_000.0,
        annual_usage_fee=500_000.0,
    )

    outputs = compute_phase1_capital_stack(inputs)

    assert outputs.senior_debt_amount == pytest.approx(60_000_000.0)
    assert outputs.equity_amount == pytest.approx(40_000_000.0)
    assert outputs.annual_debt_service > 0
    assert outputs.debt_service_coverage_ratio > 1.0
    assert outputs.annual_community_revenue == pytest.approx(1_500_000.0)


def test_invalid_debt_ratio_raises_value_error() -> None:
    bad_inputs = Phase1CapitalStackInputs(
        total_project_cost=10_000_000.0,
        senior_debt_ratio=1.2,
        annual_interest_rate=0.05,
        debt_tenor_years=10,
        annual_cash_flow_available_for_debt_service=2_000_000.0,
    )

    with pytest.raises(ValueError):
        compute_phase1_capital_stack(bad_inputs)


def test_zero_interest_rate_uses_straight_line_repayment() -> None:
    inputs = Phase1CapitalStackInputs(
        total_project_cost=10_000_000.0,
        senior_debt_ratio=0.5,
        annual_interest_rate=0.0,
        debt_tenor_years=10,
        annual_cash_flow_available_for_debt_service=2_000_000.0,
    )

    outputs = compute_phase1_capital_stack(inputs)

    # With zero interest, annual payment should be principal / years.
    assert outputs.annual_debt_service == pytest.approx(500_000.0)

