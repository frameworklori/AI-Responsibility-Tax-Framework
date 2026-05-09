"""Compute sovereignty metrics."""


def compute_concentration_index(top5_compute_capacity, total_national_compute_capacity):
    """Compute CCI = Top5ComputeProviders / TotalNationalComputeCapacity."""
    total = float(total_national_compute_capacity)
    if total <= 0:
        return 1.0
    return round(max(0.0, min(1.0, float(top5_compute_capacity) / total)), 3)


def cci_risk_level(cci):
    """Map CCI to a concentration risk level."""
    cci = max(0.0, min(1.0, float(cci)))
    if cci >= 0.8:
        return "extreme_concentration"
    if cci >= 0.6:
        return "high_concentration"
    if cci >= 0.4:
        return "moderate_concentration"
    return "distributed_capacity"
