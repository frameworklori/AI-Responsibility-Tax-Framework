"""Post-labor fiscal architecture helpers."""


def public_ai_dividend_pool(
    *,
    compute_tax,
    automation_tax,
    sovereign_ai_equity,
    infrastructure_royalties,
):
    """Aggregate AI-era public dividend funding sources."""
    total = (
        float(compute_tax)
        + float(automation_tax)
        + float(sovereign_ai_equity)
        + float(infrastructure_royalties)
    )
    return round(total, 3)


def allocate_social_dividend(pool):
    """Allocate pool across transition, dividend, and infrastructure buckets."""
    pool = float(pool)
    return {
        "reskilling_transition": round(pool * 0.4, 3),
        "public_ai_dividend": round(pool * 0.3, 3),
        "green_digital_infrastructure": round(pool * 0.3, 3),
    }
