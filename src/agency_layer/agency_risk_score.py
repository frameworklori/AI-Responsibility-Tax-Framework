"""Prototype agency-risk scoring for AI-mediated access infrastructure."""


WEIGHTS = {
    "access_concentration": 0.2,
    "preference_manipulation_risk": 0.18,
    "exit_option_weakness": 0.17,
    "allocation_dependency": 0.17,
    "participation_loss": 0.16,
    "transparency_deficit": 0.12,
}


def _validate_unit_interval(name, value):
    value = float(value)
    if value < 0.0 or value > 1.0:
        raise ValueError(f"{name} must be between 0 and 1")
    return value


def _agency_risk_label(score):
    if score < 0.25:
        return "LOW"
    if score < 0.5:
        return "MODERATE"
    if score < 0.75:
        return "HIGH"
    return "CRITICAL"


def _agency_risk_interpretation(label):
    interpretations = {
        "LOW": "Access systems appear broadly contestable, with limited agency loss.",
        "MODERATE": "Agency risk is emerging and should be monitored through access governance.",
        "HIGH": "Concentrated access and allocation dependency may weaken human economic agency.",
        "CRITICAL": "Access infrastructure may be creating severe dependency and agency loss.",
    }
    return interpretations[label]


def calculate_agency_risk(
    access_concentration,
    preference_manipulation_risk,
    exit_option_weakness,
    allocation_dependency,
    participation_loss,
    transparency_deficit,
):
    """Calculate an AIRTF agency-layer risk score from normalized inputs."""
    inputs = {
        "access_concentration": access_concentration,
        "preference_manipulation_risk": preference_manipulation_risk,
        "exit_option_weakness": exit_option_weakness,
        "allocation_dependency": allocation_dependency,
        "participation_loss": participation_loss,
        "transparency_deficit": transparency_deficit,
    }
    normalized = {
        name: _validate_unit_interval(name, value) for name, value in inputs.items()
    }
    score = round(sum(normalized[name] * weight for name, weight in WEIGHTS.items()), 3)
    score = max(0.0, min(1.0, score))
    label = _agency_risk_label(score)
    return {
        "score": score,
        "label": label,
        "interpretation": _agency_risk_interpretation(label),
    }

