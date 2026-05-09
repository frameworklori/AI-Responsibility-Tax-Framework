"""Social stability and transition metrics."""


def automation_shock_velocity(workers_displaced, time_window_months):
    """Compute ASV = WorkersDisplaced / TimeWindow."""
    months = float(time_window_months)
    if months <= 0:
        raise ValueError("time_window_months must be > 0")
    return round(float(workers_displaced) / months, 3)


def ai_social_stability_index(
    *,
    youth_unemployment,
    middle_class_erosion,
    ai_anxiety,
    wage_stagnation,
    compute_concentration,
    housing_stress,
):
    """Return a simple risk-oriented ASSI score where higher means less stable."""
    values = [
        youth_unemployment,
        middle_class_erosion,
        ai_anxiety,
        wage_stagnation,
        compute_concentration,
        housing_stress,
    ]
    bounded = [max(0.0, min(1.0, float(value))) for value in values]
    return round(sum(bounded) / len(bounded), 3)


def stability_level(assi):
    """Map ASSI risk score to a readable stability level."""
    assi = max(0.0, min(1.0, float(assi)))
    if assi >= 0.75:
        return "critical_instability_risk"
    if assi >= 0.55:
        return "elevated_transition_risk"
    if assi >= 0.35:
        return "moderate_transition_risk"
    return "stable_transition"
