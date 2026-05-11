import unittest

from src.current_signals.asset_real_divergence import calculate_asset_real_divergence


class AssetRealDivergenceTests(unittest.TestCase):
    def test_low_signal(self):
        result = calculate_asset_real_divergence(0.1, 0.05, 0.1, 0.05)
        self.assertEqual(result["label"], "LOW")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 1)

    def test_critical_signal(self):
        result = calculate_asset_real_divergence(0.9, 0.9, 0.95, 0.85)
        self.assertEqual(result["label"], "CRITICAL")
        self.assertGreaterEqual(result["score"], 0.75)

    def test_threshold_labels(self):
        self.assertEqual(
            calculate_asset_real_divergence(0.25, 0.25, 0.25, 0.25)["label"],
            "MODERATE",
        )
        self.assertEqual(
            calculate_asset_real_divergence(0.5, 0.5, 0.5, 0.5)["label"],
            "HIGH",
        )

    def test_invalid_inputs_raise(self):
        with self.assertRaises(ValueError):
            calculate_asset_real_divergence(-0.01, 0.1, 0.1, 0.1)
        with self.assertRaises(ValueError):
            calculate_asset_real_divergence(0.1, 0.1, 1.01, 0.1)


if __name__ == "__main__":
    unittest.main()
