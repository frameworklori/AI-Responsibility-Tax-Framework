"""AI Responsibility Tax model."""


def responsibility_tax(
    *,
    profit,
    unemployment_impact,
    energy_consumption,
    alpha=0.08,
    beta=0.15,
    gamma=0.05,
):
    """Compute RT = alpha*Profit + beta*UnemploymentImpact + gamma*EnergyConsumption."""
    return round(
        (alpha * float(profit))
        + (beta * float(unemployment_impact))
        + (gamma * float(energy_consumption)),
        3,
    )
