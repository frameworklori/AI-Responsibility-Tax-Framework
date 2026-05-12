import unittest

from src.agency_layer.agency_risk_score import calculate_agency_risk


class AgencyRiskScoreTests(unittest.TestCase):
    def test_valid_low_score(self):
        result = calculate_agency_risk(0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
        self.assertEqual(result["score"], 0.1)
        self.assertEqual(result["label"], "LOW")
        self.assertIn("contestable", result["interpretation"])

    def test_valid_critical_score(self):
        result = calculate_agency_risk(0.9, 0.9, 0.9, 0.9, 0.9, 0.9)
        self.assertEqual(result["score"], 0.9)
        self.assertEqual(result["label"], "CRITICAL")

    def test_invalid_input_below_zero(self):
        with self.assertRaises(ValueError):
            calculate_agency_risk(-0.1, 0.2, 0.2, 0.2, 0.2, 0.2)

    def test_invalid_input_above_one(self):
        with self.assertRaises(ValueError):
            calculate_agency_risk(0.2, 1.1, 0.2, 0.2, 0.2, 0.2)

    def test_score_remains_within_zero_and_one(self):
        result = calculate_agency_risk(1, 1, 1, 1, 1, 1)
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 1)

    def test_labels_follow_thresholds(self):
        self.assertEqual(
            calculate_agency_risk(0.24, 0.24, 0.24, 0.24, 0.24, 0.24)["label"],
            "LOW",
        )
        self.assertEqual(
            calculate_agency_risk(0.25, 0.25, 0.25, 0.25, 0.25, 0.25)["label"],
            "MODERATE",
        )
        self.assertEqual(
            calculate_agency_risk(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)["label"],
            "HIGH",
        )
        self.assertEqual(
            calculate_agency_risk(0.75, 0.75, 0.75, 0.75, 0.75, 0.75)["label"],
            "CRITICAL",
        )


if __name__ == "__main__":
    unittest.main()

