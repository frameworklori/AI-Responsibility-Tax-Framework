"""Civilization liquidity and demand fragility helpers."""


def circulation_risk_score(
    *,
    productivity_growth,
    median_income_growth,
    money_velocity_change,
    household_debt_growth,
    wealth_concentration_growth,
):
    """Estimate circulation risk from productivity-income divergence and debt stress."""
    productivity_gap = max(0.0, float(productivity_growth) - float(median_income_growth))
    velocity_stress = max(0.0, -float(money_velocity_change))
    values = [
        min(1.0, productivity_gap),
        min(1.0, velocity_stress),
        max(0.0, min(1.0, float(household_debt_growth))),
        max(0.0, min(1.0, float(wealth_concentration_growth))),
    ]
    return round(sum(values) / len(values), 3)


def mpc_weighted_circulation(low_income_share, middle_income_share, high_income_share):
    """Estimate circulation speed from income distribution using rough MPC weights."""
    return round(
        (0.9 * float(low_income_share))
        + (0.75 * float(middle_income_share))
        + (0.35 * float(high_income_share)),
        3,
    )
