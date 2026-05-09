"""AI-linked displacement score."""


def ai_linked_displacement_score(
    *,
    ai_adoption_rate,
    workforce_compression_speed,
    revenue_per_employee_growth,
    human_to_ai_replacement_ratio,
    ai_generated_output_ratio,
    department_automation_evidence,
):
    """Estimate how strongly displacement appears linked to AI adoption."""
    values = [
        ai_adoption_rate,
        workforce_compression_speed,
        revenue_per_employee_growth,
        human_to_ai_replacement_ratio,
        ai_generated_output_ratio,
        department_automation_evidence,
    ]
    bounded = [max(0.0, min(1.0, float(value))) for value in values]
    return round(sum(bounded) / len(bounded), 3)
