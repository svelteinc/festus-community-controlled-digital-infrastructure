"""Simple DSCR and capital stack sensitivity helpers.

These helpers build on :mod:`src.simulator.capital_stack` to explore how
changes in key parameters (interest rate, senior debt ratio) affect DSCR and
capital structure. They are intentionally lightweight and meant for
order-of-magnitude policy discussions, not detailed project finance modeling.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Iterable, List

from src.simulator.capital_stack import (
    Phase1CapitalStackInputs,
    Phase1CapitalStackOutputs,
    compute_phase1_capital_stack,
)


def sweep_interest_rate(
    base_inputs: Phase1CapitalStackInputs,
    rates: Iterable[float],
) -> List[Phase1CapitalStackOutputs]:
    """Compute outputs for a range of interest rates.

    All inputs except ``annual_interest_rate`` are held constant. This is useful
    for understanding how lenders' pricing affects DSCR and equity needs.
    """

    outputs: List[Phase1CapitalStackOutputs] = []
    for rate in rates:
        scenario_inputs = replace(base_inputs, annual_interest_rate=rate)
        outputs.append(compute_phase1_capital_stack(scenario_inputs))
    return outputs


def sweep_senior_debt_ratio(
    base_inputs: Phase1CapitalStackInputs,
    debt_ratios: Iterable[float],
) -> List[Phase1CapitalStackOutputs]:
    """Compute outputs for a range of senior debt ratios.

    All inputs except ``senior_debt_ratio`` are held constant. This is useful
    for exploring trade-offs between leverage, DSCR, and required equity.
    """

    outputs: List[Phase1CapitalStackOutputs] = []
    for ratio in debt_ratios:
        scenario_inputs = replace(base_inputs, senior_debt_ratio=ratio)
        outputs.append(compute_phase1_capital_stack(scenario_inputs))
    return outputs

