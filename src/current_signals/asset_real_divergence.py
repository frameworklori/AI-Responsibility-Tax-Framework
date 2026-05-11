"""Asset-market versus real-economy divergence signal."""


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


def calculate_asset_real_divergence(
    stock_market_strength,
    wage_growth_weakness,
    household_cashflow_stress,
    concentration_index,
):
    """Estimate divergence between asset strength and household liquidity."""
    weights = {
        "stock_market_strength": 0.25,
        "wage_growth_weakness": 0.25,
        "household_cashflow_stress": 0.30,
        "concentration_index": 0.20,
    }
    values = {
        "stock_market_strength": stock_market_strength,
        "wage_growth_weakness": wage_growth_weakness,
        "household_cashflow_stress": household_cashflow_stress,
        "concentration_index": concentration_index,
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
        "interpretation": (
            f"{label} asset-real divergence: asset prices and concentrated ownership "
            "are moving ahead of wage circulation and household cash-flow resilience."
        ),
    }
