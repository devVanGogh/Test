import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from signal_research_sandbox.decision_audit import audit_decisions, brier_score
from signal_research_sandbox.rumor_quality import event_fingerprint, inspect_event
from signal_research_sandbox.defensive_stress import simulate_linear_shock, concentration_hhi
from signal_research_sandbox.anomaly_probe import lagged_pearson

class SyntheticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "fixtures/synthetic_cases.json").read_text(encoding="utf-8"))

    def test_hold_rate(self):
        r = audit_decisions(self.data["decisions"])
        self.assertEqual(r["sample_size"], 4)
        self.assertEqual(r["hold_rate"], .5)
        self.assertEqual(r["trade_coverage"], .5)
        self.assertEqual(r["conditional_accuracy"], .5)

    def test_empty_hold(self):
        self.assertIsNone(audit_decisions([])["hold_rate"])

    def test_invalid_action(self):
        with self.assertRaises(ValueError):
            audit_decisions([{"action": "AUTO_BUY"}])

    def test_brier(self):
        self.assertAlmostEqual(brier_score([.8, .2], [True, False]), .04)

    def test_invalid_probability(self):
        with self.assertRaises(ValueError):
            brier_score([1.5], [False])

    def test_rumor_flags(self):
        x = inspect_event(self.data["rumor"], "2020-01-02T09:01:00Z")
        self.assertIn("guaranteed profit", x["risk_flags"])
        self.assertIsNone(x["predicted_probability"])

    def test_rumor_future_data(self):
        with self.assertRaises(ValueError):
            inspect_event(self.data["rumor"], "2020-01-01T09:00:00Z")

    def test_no_source_permission(self):
        event = dict(self.data["rumor"], access_granted=False)
        with self.assertRaises(PermissionError):
            inspect_event(event, "2020-01-03T09:00:00Z")

    def test_dedup(self):
        self.assertEqual(event_fingerprint(" HELLO  world "), event_fingerprint("hello world"))

    def test_shock(self):
        x = self.data["stress"]
        self.assertAlmostEqual(simulate_linear_shock(x["factor_exposures"], x["hypothetical_shocks"]), -.064)

    def test_missing_factor(self):
        with self.assertRaises(ValueError):
            simulate_linear_shock({"f": .5}, {})

    def test_hhi(self):
        self.assertAlmostEqual(concentration_hhi([.5, .5]), .5)

    def test_bad_hhi(self):
        with self.assertRaises(ValueError):
            concentration_hhi([.6, .6])

    def test_lagged_corr(self):
        self.assertAlmostEqual(lagged_pearson([1,2,3,4,5], [0,2,4,6,8], 1), 1.0)

    def test_constant_corr(self):
        self.assertIsNone(lagged_pearson([1,1,1,1,1], [1,2,3,4,5], 1))

    def test_invalid_lag(self):
        with self.assertRaises(ValueError):
            lagged_pearson([1,2,3,4], [1,2,3,4], 0)

if __name__ == "__main__":
    unittest.main()
