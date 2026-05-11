"""U.S. trade deficit and demand dependency signal."""


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


def calculate_trade_demand_dependency(
    trade_deficit_ratio,
    import_dependency,
    consumer_credit_dependency,
    wage_income_stress,
    dollar_reserve_support,
):
    """Estimate demand fragility behind import-heavy U.S. consumption."""
    weights = {
        "trade_deficit_ratio": 0.20,
        "import_dependency": 0.20,
        "consumer_credit_dependency": 0.22,
        "wage_income_stress": 0.25,
        "dollar_reserve_support": 0.13,
    }
    values = {
        "trade_deficit_ratio": trade_deficit_ratio,
        "import_dependency": import_dependency,
        "consumer_credit_dependency": consumer_credit_dependency,
        "wage_income_stress": wage_income_stress,
        "dollar_reserve_support": dollar_reserve_support,
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
            f"{label} trade-demand dependency: import-heavy consumption is relying "
            "on credit, wage resilience, and dollar support to keep demand circulating."
        ),
    }
