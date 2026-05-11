import unittest

from src.current_signals.liquidity_stress_signal import calculate_liquidity_stress


class LiquidityStressSignalTests(unittest.TestCase):
    def test_low_signal(self):
        result = calculate_liquidity_stress(0.05, 0.1, 0.1, 0.05, 0.1, 0.05)
        self.assertEqual(result["label"], "LOW")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 1)

    def test_critical_signal(self):
        result = calculate_liquidity_stress(0.9, 0.95, 0.9, 0.85, 0.8, 0.9)
        self.assertEqual(result["label"], "CRITICAL")
        self.assertGreaterEqual(result["score"], 0.75)

    def test_threshold_labels(self):
        self.assertEqual(
            calculate_liquidity_stress(0.25, 0.25, 0.25, 0.25, 0.25, 0.25)["label"],
            "MODERATE",
        )
        self.assertEqual(
            calculate_liquidity_stress(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)["label"],
            "HIGH",
        )

    def test_invalid_inputs_raise(self):
        with self.assertRaises(ValueError):
            calculate_liquidity_stress(-0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
        with self.assertRaises(ValueError):
            calculate_liquidity_stress(0.1, 1.1, 0.1, 0.1, 0.1, 0.1)


if __name__ == "__main__":
    unittest.main()
