"""Current U.S. liquidity stress signal for AIRTF prototypes."""


THRESHOLDS = (
    (0.75, "CRITICAL"),
    (0.50, "HIGH"),
    (0.25, "MODERATE"),
    (0.00, "LOW"),
)


def _validate_normalized(name, value):
    value = float(value)
    if value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must be normalized between 0 and 1")
    return value


def _label(score):
    for minimum, label in THRESHOLDS:
        if score >= minimum:
            return label
    return "LOW"


def calculate_liquidity_stress(
    layoff_index,
    consumer_debt_stress,
    real_wage_pressure,
    credit_dependency,
    asset_market_divergence,
    deficit_dependency,
):
    """Estimate household liquidity stress from normalized current signals."""
    weights = {
        "layoff_index": 0.18,
        "consumer_debt_stress": 0.20,
        "real_wage_pressure": 0.20,
        "credit_dependency": 0.17,
        "asset_market_divergence": 0.13,
        "deficit_dependency": 0.12,
    }
    values = {
        "layoff_index": layoff_index,
        "consumer_debt_stress": consumer_debt_stress,
        "real_wage_pressure": real_wage_pressure,
        "credit_dependency": credit_dependency,
        "asset_market_divergence": asset_market_divergence,
        "deficit_dependency": deficit_dependency,
    }
    score = sum(
        _validate_normalized(name, value) * weights[name]
        for name, value in values.items()
    )
    score = round(score, 3)
    label = _label(score)
    return {
        "score": score,
        "label": label,
        "explanation": (
            f"{label} liquidity stress: household cash-flow pressure is driven by "
            "labor compression, debt reliance, weak real wages, market-real economy "
            "divergence, and dependence on deficit support."
        ),
    }
