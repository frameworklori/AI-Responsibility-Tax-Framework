"""Integration-layer monopoly risk helpers."""


def integration_layer_monopoly_score(
    *,
    layers_controlled,
    acquisition_velocity,
    api_dependency,
    distribution_control,
    compute_dependency,
):
    """Estimate cross-layer integration monopoly risk in [0, 1]."""
    layer_score = min(1.0, max(0.0, float(layers_controlled)) / 5.0)
    values = [
        layer_score,
        acquisition_velocity,
        api_dependency,
        distribution_control,
        compute_dependency,
    ]
    bounded = [max(0.0, min(1.0, float(value))) for value in values]
    return round(sum(bounded) / len(bounded), 3)


def monopoly_risk_level(score):
    """Map integration monopoly score to a readable level."""
    score = max(0.0, min(1.0, float(score)))
    if score >= 0.75:
        return "critical_integration_monopoly_risk"
    if score >= 0.55:
        return "high_integration_monopoly_risk"
    if score >= 0.35:
        return "moderate_integration_risk"
    return "low_integration_risk"
