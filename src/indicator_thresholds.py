"""Provisional falsifiability thresholds for AIRTF."""


def compute_concentration_status(cci):
    cci = float(cci)
    if cci > 0.8:
        return "crisis"
    if cci > 0.6:
        return "warning"
    return "normal"


def demand_fragility_status(productivity_growth_years_above_income, median_real_power_declining):
    if median_real_power_declining:
        return "crisis"
    if productivity_growth_years_above_income >= 3:
        return "warning"
    return "normal"


def platform_rent_status(platform_fee_growth, gdp_growth, labor_income_growth):
    if platform_fee_growth > labor_income_growth:
        return "crisis"
    if platform_fee_growth > gdp_growth:
        return "warning"
    return "normal"
