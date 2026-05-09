"""AI Layered Value Extraction Model."""

RISK_VALUES = {
    "low": 0.25,
    "medium": 0.5,
    "high": 0.75,
    "extreme": 1.0,
    "variable": 0.45,
}


def layered_value_extraction_score(
    *,
    profit_density,
    monopoly_intensity,
    social_externality,
    infrastructure_dependence,
    labor_replacement_scale,
):
    """Return a simple ALVEM risk score in [0, 1]."""
    values = [
        _as_score(profit_density),
        _as_score(monopoly_intensity),
        _as_score(social_externality),
        _as_score(infrastructure_dependence),
        _as_score(labor_replacement_scale),
    ]
    return round(sum(values) / len(values), 3)


def _as_score(value):
    if isinstance(value, str):
        return RISK_VALUES[value.lower()]
    return max(0.0, min(1.0, float(value)))
