from dataclasses import dataclass


@dataclass
class Phase1CapitalStackInputs:
    """Input parameters for a simple Phase 1 capital stack model.

    This is a conceptual helper for order-of-magnitude thinking only. It does
    not constitute financial advice or a full project finance model.

    You can work directly in dollars or also specify capacity in MW and
    per-MW fees to make assumptions more explicit.
    """

    total_project_cost: float
    senior_debt_ratio: float
    annual_interest_rate: float
    debt_tenor_years: int
    annual_cash_flow_available_for_debt_service: float
    annual_ground_rent: float = 0.0
    annual_usage_fee: float = 0.0
    capacity_mw: float | None = None
    ground_rent_per_mw: float = 0.0
    usage_fee_per_mw: float = 0.0


@dataclass
class Phase1CapitalStackOutputs:
    """Computed quantities for the Phase 1 capital stack."""

    senior_debt_amount: float
    equity_amount: float
    annual_debt_service: float
    debt_service_coverage_ratio: float
    annual_community_revenue: float


def _validate_inputs(inputs: Phase1CapitalStackInputs) -> None:
    """Validate basic numerical ranges.

    Raises:
        ValueError: If any input is outside a reasonable range.
    """

    if inputs.total_project_cost <= 0:
        raise ValueError("total_project_cost must be positive")
    if not 0.0 < inputs.senior_debt_ratio < 1.0:
        raise ValueError("senior_debt_ratio must be between 0 and 1")
    if inputs.debt_tenor_years <= 0:
        raise ValueError("debt_tenor_years must be positive")
    if inputs.annual_cash_flow_available_for_debt_service <= 0:
        raise ValueError(
            "annual_cash_flow_available_for_debt_service must be positive",
        )
    if inputs.annual_interest_rate < 0:
        raise ValueError("annual_interest_rate cannot be negative")
    if inputs.capacity_mw is not None and inputs.capacity_mw < 0:
        raise ValueError("capacity_mw cannot be negative")
    if inputs.ground_rent_per_mw < 0:
        raise ValueError("ground_rent_per_mw cannot be negative")
    if inputs.usage_fee_per_mw < 0:
        raise ValueError("usage_fee_per_mw cannot be negative")


def _annuity_payment(principal: float, rate: float, years: int) -> float:
    """Compute a simple level annual payment for fully amortizing debt.

    Args:
        principal: Loan amount.
        rate: Annual interest rate as a decimal (e.g., 0.06 for 6%).
        years: Number of years over which the loan amortizes.

    Returns:
        The constant annual payment required to amortize the principal.
    """

    if years <= 0:
        raise ValueError("years must be positive")

    if rate == 0:
        return principal / years

    factor = (1 + rate) ** (-years)
    return rate * principal / (1 - factor)


def compute_phase1_capital_stack(
    inputs: Phase1CapitalStackInputs,
) -> Phase1CapitalStackOutputs:
    """Compute a simple Phase 1 capital stack and basic ratios.

    The model assumes:
    - Senior debt is a fixed percentage of total project cost.
    - Debt amortizes in equal annual payments over the tenor.
    - DSCR is calculated using cash flow available for debt service
      *before* community fees.
    - Community revenues include annual ground rent and usage fees. If per-MW
      fees are provided and the corresponding annual value is zero, per-MW
      values are used to derive annual community revenue.
    """

    _validate_inputs(inputs)

    senior_debt_amount = inputs.total_project_cost * inputs.senior_debt_ratio
    equity_amount = inputs.total_project_cost - senior_debt_amount

    annual_debt_service = _annuity_payment(
        principal=senior_debt_amount,
        rate=inputs.annual_interest_rate,
        years=inputs.debt_tenor_years,
    )

    dscr = inputs.annual_cash_flow_available_for_debt_service / annual_debt_service

    community_revenue = inputs.annual_ground_rent + inputs.annual_usage_fee
    if inputs.capacity_mw is not None and inputs.capacity_mw > 0:
        if inputs.ground_rent_per_mw > 0 and inputs.annual_ground_rent == 0.0:
            community_revenue += inputs.capacity_mw * inputs.ground_rent_per_mw
        if inputs.usage_fee_per_mw > 0 and inputs.annual_usage_fee == 0.0:
            community_revenue += inputs.capacity_mw * inputs.usage_fee_per_mw

    return Phase1CapitalStackOutputs(
        senior_debt_amount=senior_debt_amount,
        equity_amount=equity_amount,
        annual_debt_service=annual_debt_service,
        debt_service_coverage_ratio=dscr,
        annual_community_revenue=community_revenue,
    )

