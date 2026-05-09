import unittest

from src.compute_sovereignty import compute_concentration_index, cci_risk_level
from src.displacement_score import ai_linked_displacement_score
from src.integration_monopoly import (
    integration_layer_monopoly_score,
    monopoly_risk_level,
)
from src.post_labor_fiscal import allocate_social_dividend, public_ai_dividend_pool
from src.responsibility_tax import responsibility_tax
from src.social_stability import (
    ai_social_stability_index,
    automation_shock_velocity,
    stability_level,
)
from src.value_extraction import layered_value_extraction_score


class AIRTFV2ModelTests(unittest.TestCase):
    def test_responsibility_tax_positive(self):
        tax = responsibility_tax(
            profit=1000,
            unemployment_impact=200,
            energy_consumption=100,
        )
        self.assertGreater(tax, 0)

    def test_compute_concentration_index(self):
        cci = compute_concentration_index(800, 1000)
        self.assertEqual(cci, 0.8)
        self.assertEqual(cci_risk_level(cci), "extreme_concentration")

    def test_value_extraction_score(self):
        score = layered_value_extraction_score(
            profit_density="extreme",
            monopoly_intensity="high",
            social_externality="high",
            infrastructure_dependence="extreme",
            labor_replacement_scale="medium",
        )
        self.assertGreater(score, 0.7)

    def test_social_dividend_allocation(self):
        pool = public_ai_dividend_pool(
            compute_tax=100,
            automation_tax=50,
            sovereign_ai_equity=25,
            infrastructure_royalties=25,
        )
        allocation = allocate_social_dividend(pool)
        self.assertEqual(pool, 200)
        self.assertEqual(allocation["reskilling_transition"], 80)

    def test_automation_shock_velocity(self):
        self.assertEqual(automation_shock_velocity(120000, 12), 10000)

    def test_assi_level(self):
        assi = ai_social_stability_index(
            youth_unemployment=0.22,
            middle_class_erosion=0.48,
            ai_anxiety=0.64,
            wage_stagnation=0.55,
            compute_concentration=0.78,
            housing_stress=0.5,
        )
        self.assertEqual(stability_level(assi), "moderate_transition_risk")

    def test_ai_linked_displacement_score(self):
        score = ai_linked_displacement_score(
            ai_adoption_rate=0.8,
            workforce_compression_speed=0.7,
            revenue_per_employee_growth=0.65,
            human_to_ai_replacement_ratio=0.6,
            ai_generated_output_ratio=0.75,
            department_automation_evidence=0.8,
        )
        self.assertGreater(score, 0.7)

    def test_integration_layer_monopoly_score(self):
        score = integration_layer_monopoly_score(
            layers_controlled=4,
            acquisition_velocity=0.8,
            api_dependency=0.7,
            distribution_control=0.85,
            compute_dependency=0.9,
        )
        self.assertEqual(monopoly_risk_level(score), "critical_integration_monopoly_risk")


if __name__ == "__main__":
    unittest.main()
