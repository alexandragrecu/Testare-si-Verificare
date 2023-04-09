from main import min_cost_to_buy_stamps

"""
The decisions in the code are:
    1. if not (1 <= N <= 1000)
    2. if not (1 <= M <= 10000)
    3. if not (1 <= K <= 1000)
    4. if len(intervals) != M
    5. for i, (mi, ci) in enumerate(intervals):
        5.a. if not (1 <= mi <= 100000)
        5.b. if not (1 <= ci <= 10000)
    6. while N > 0
    7. while i >= 0 and intervals[i][0] >= N
    8. if cost
"""

test_cases = [
    (0, 1, 1, [(1, 1)], "N (Numarul de pagini) trebuie sa fie intre 1 si 1000"),
    (1, 0, 1, [], "M (Numarul de intervale) trebuie sa fie intre 1 si 10000"),
    (1, 1, 0, [(1, 1)], "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000"),
    (1, 1, 1, [(1, 1), (2, 1)], "Numarul de perechi (mi, ci) trebuie sa fie M"),
    (1, 1, 1, [(0, 1)], "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)"),
    (1, 1, 1, [(1, 0)], "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)"),
    (4, 3, 2, [(5, 3), (2, 1), (6, 2)], 3), # input valid + solutie valida
]

for i, (N, M, K, intervals, expected_output) in enumerate(test_cases, start=1):
    result = min_cost_to_buy_stamps((N, M, K, intervals))
    assert result == expected_output, f"Test {i} failed: expected {expected_output}, got {result}"
    print(f"Test {i} passed")

