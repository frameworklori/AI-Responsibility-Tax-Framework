import unittest

from src.current_signals.trade_demand_dependency import (
    calculate_trade_demand_dependency,
)


class TradeDemandDependencyTests(unittest.TestCase):
    def test_low_signal(self):
        result = calculate_trade_demand_dependency(0.1, 0.05, 0.1, 0.05, 0.1)
        self.assertEqual(result["label"], "LOW")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 1)

    def test_critical_signal(self):
        result = calculate_trade_demand_dependency(0.9, 0.85, 0.95, 0.9, 0.8)
        self.assertEqual(result["label"], "CRITICAL")
        self.assertGreaterEqual(result["score"], 0.75)

    def test_threshold_labels(self):
        self.assertEqual(
            calculate_trade_demand_dependency(0.25, 0.25, 0.25, 0.25, 0.25)[
                "label"
            ],
            "MODERATE",
        )
        self.assertEqual(
            calculate_trade_demand_dependency(0.5, 0.5, 0.5, 0.5, 0.5)["label"],
            "HIGH",
        )

    def test_invalid_inputs_raise(self):
        with self.assertRaises(ValueError):
            calculate_trade_demand_dependency(-0.1, 0.1, 0.1, 0.1, 0.1)
        with self.assertRaises(ValueError):
            calculate_trade_demand_dependency(0.1, 0.1, 0.1, 0.1, 1.1)


if __name__ == "__main__":
    unittest.main()
