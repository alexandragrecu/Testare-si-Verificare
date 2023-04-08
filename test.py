import unittest
from main import min_cost_to_buy_stamps

class TestStampMinCost(unittest.TestCase):
    def test_equivalence_partitioning(self):
        equivalence_partitioning_cases = [
            # Valid partitions
            ((1, 1, 1, [(1, 1)]), 1),  # N, M, and K all have minimum valid values
            ((5, 3, 2, [(3, 1), (6, 2), (8, 3)]), 6),  # N, M, and K have arbitrary valid values

            # Invalid partitions
            ((0, 1, 1, [(1, 1)]), "N (Number of pages) should be between 1 and 1000"),  # Invalid N, too small
            ((1001, 1, 1, [(1, 1)]), "N (Number of pages) should be between 1 and 1000"),  # Invalid N, too large
            ((1, 0, 1, [(1, 1)]), "M (Number of intervals) should be between 1 and 10000"),  # Invalid M, too small
            ((1, 10001, 1, [(1, 1)]), "M (Number of intervals) should be between 1 and 10000"),  # Invalid M, too large
            ((1, 1, 0, [(1, 1)]), "K (Maximum length of intervals) should be between 1 and 1000"),
            # Invalid K, too small
            ((1, 1, 1001, [(1, 1)]), "K (Maximum length of intervals) should be between 1 and 1000"),
            # Invalid K, too large
            ((1, 1, 1, [(0, 1)]), "mi (Upper limit of interval i) should be between (0, 10000)"),
            # Invalid mi, too small
            ((1, 1, 1, [(100000, 1)]), "mi (Upper limit of interval i) should be between (0, 10000)"),
            # Invalid mi, too large
            ((1, 1, 1, [(1, 0)]), "ci (Cost of interval i) should be between (0 and 10000)"),  # Invalid ci, too small
            ((1, 1, 1, [(1, 10000)]), "ci (Cost of interval i) should be between (0 and 10000)")  # Invalid ci, too large
        ]

        # for i, (input_tuple, expected) in enumerate(equivalence_partitioning_cases):
        #     with self.assertRaises(Exception) if isinstance(expected, str) else self.subTest(i=i):
        #         result = min_cost_to_buy_stamps(input_tuple)
        #         self.assertEqual(result, expected, f"Equivalence partitioning Test: Failed at case {i + 1}")

        for i, (input_tuple, expected) in enumerate(equivalence_partitioning_cases):
            result = min_cost_to_buy_stamps(input_tuple)
            self.assertEqual(result, expected, f"Boundary value analysis Test: Failed at case {i + 1}")


    # def test_boundary_value(self):
    #     boundary_value_cases = [
    #         ((2, 1, 1, [(1, 1)]), 0),  # case 1: N is just above the minimum value, M and K at the minimum value
    #         ((999, 10000, 999, [(i, i) for i in range(1, 10001)]), 999),  # case 2: N and K are just below the maximum value, M at the maximum value
    #     ]
    #
    #     for i, (input_tuple, expected) in enumerate(boundary_value_cases):
    #         result = min_cost_to_buy_stamps(input_tuple)
    #         self.assertEqual(result, expected, f"Boundary value analysis Test: Failed at case {i + 1}")
    #
    # def test_cause_effect(self):
    #     cause_effect_graph_cases = [
    #         ((4, 3, 2, [(3, 1), (6, 2), (8, 3)]), 3),  # test with an arbitrary combination of input conditions
    #         ((4, 4, 1, [(1, 1), (2, 2), (3, 3), (4, 4)]), 10),  # test with overlapping intervals
    #         ((5, 2, 5, [(3, 1), (8, 3)]), 3),  # test with a single subsequence covering all pages
    #     ]
    #
    #     for i, (input_tuple, expected) in enumerate(cause_effect_graph_cases):
    #         result = min_cost_to_buy_stamps(input_tuple)
    #         self.assertEqual(result, expected, f"Cause Effect Test: Failed at case {i + 1}")


if __name__ == "__main__":
    unittest.main()