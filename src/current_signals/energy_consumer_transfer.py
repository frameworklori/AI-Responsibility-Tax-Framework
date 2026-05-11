"""Energy shock transfer signal from consumers to producers."""


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


def calculate_energy_consumer_transfer(
    oil_price_pressure,
    gasoline_cost_pressure,
    utility_cost_pressure,
    energy_export_gain,
    household_income_pressure,
):
    """Estimate consumer fragility caused by energy-linked cost transfers."""
    weights = {
        "oil_price_pressure": 0.20,
        "gasoline_cost_pressure": 0.22,
        "utility_cost_pressure": 0.18,
        "energy_export_gain": 0.15,
        "household_income_pressure": 0.25,
    }
    values = {
        "oil_price_pressure": oil_price_pressure,
        "gasoline_cost_pressure": gasoline_cost_pressure,
        "utility_cost_pressure": utility_cost_pressure,
        "energy_export_gain": energy_export_gain,
        "household_income_pressure": household_income_pressure,
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
            f"{label} energy-consumer transfer: energy producer gains and higher "
            "essential costs are pressuring household liquidity and demand resilience."
        ),
    }
