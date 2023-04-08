import unittest
from main import min_cost_to_buy_stamps

"""
Clasele intrarilor: 
    - N (Numarul de pagini ale clasorului) 0 < N < 1001
    - M (Numarul de intervale de timbre) 0 < M < 10001
    - K (Lungimea maxima a unei subsecvente de timbre care poate fi luata din interval) 0 < K < 1001
    - (mi, ci) i <= M:   
        - mi (Marginea superioara a intervalului i) 0 < mi < 100 000, i <= M
        - ci (Costul intervalului i) 0 < ci < 10 000, i <= M
    1) N:
    N_1 = {N | 0 < N < 1001} # N valid
    N_2 = {N | N < 1} # N invalid
    N_3 = {N | N > 1001} # N invalid
    2) M:
    M_1 = {M | 0 > M < 10001} # M valid
    M_2 = {M | M < 1} # M invalid
    M_3 = {M | M > 10001} # M invalid
    3) K:
    K_1 = {K | 0 < K < 1001} # K valid
    K_2 = {K | K < 1} # K invalid
    K_3 = {K | K > 10001} # K invalid
    4) mi:
    mi_1 = {m[i] | 0 < m[i] < 100 000, 0 < i < M} # mi valid
    mi_2 = {m[i] | m[i] < 0, 0 < i < M} # mi invalid
    mi_3 = {m[i] | m[i] > 100 000, 0 < i < M} # mi invalid
    mi_4 = {m[i] | 0 < m[i] < 100 000, count((m[i], c[i])) != M} # numarul total de perechi (mi, ci) este invalid
    5) ci:
    ci_1 = {c[i] | 0 < c[i] < 10 000, 0 < i <= M} # ci valid
    ci_2 = {c[i] | c[i] < 0, 0 < i <= M} # ci invalid
    ci_3 = {c[i] | c[i] > 10 000, 0 < i <= M} # ci invalid
    ci_4 = {c[i] | 0 < c[i] < 10 000, count((m[i], c[i])) != M} # numarul total de perechi (mi, ci) este invalid
------------------------------------------------------------------------------
    Clase iesiri:
    i_1 = Solutia dorita (toate datele de intrare sunt valide)
    i_2 = "N (Numarul de pagini) trebuie sa fie intre 1 si 1000"
    i_3 = "M (Numarul de intervale) trebuie sa fie intre 1 si 10000"
    i_4 = "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000"
    i_5 = "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 10000)"
    i_6 = "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)"
    i_7 = "Numarul de perechi (mi, ci) trebuie sa fie M"
------------------------------------------------------------------------------
    Clase de echivalenta finala:
    C_1 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_1, ci in ci_1 si iesirea i_1}
    C_2 = {N, M, K, (mi, ci) | N in N_2, M in M_1, K in K_1, mi in mi_1, ci in ci_1 si iesirea i_2}
    C_3 = {N, M, K, (mi, ci) | N in N_3, M in M_1, K in K_1, mi in mi_1, ci in ci_1 si iesirea i_2}
    C_4 = {N, M, K, (mi, ci) | N in N_1, M in M_2, K in K_1, mi in mi_1, ci in ci_1 si iesirea i_3}
    C_5 = {N, M, K, (mi, ci) | N in N_1, M in M_3, K in K_1, mi in mi_1, ci in ci_1 si iesirea i_3}
    C_6 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_2, mi in mi_1, ci in ci_1 si iesirea i_4}
    C_7 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_3, mi in mi_1, ci in ci_1 si iesirea i_4}
    C_8 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_2, ci in ci_1 si iesirea i_5}
    C_9 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_3, ci in ci_1 si iesirea i_5}
    C_10 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_1, ci in ci_2 si iesirea i_6}
    C_11 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_1, ci in ci_3 si iesirea i_6}
    C_12 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_4, ci in ci_4 si iesirea i_7}
"""

class TestStampMinCost(unittest.TestCase):
    def test_C_1(self):
        # input bun
        N, M, K, intervals, expected = (5, 3, 2, [(3, 1), (6, 2), (8, 3)], 6)
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_2(self):
        # N < 1
        N, M, K, intervals, expected = (
        0, 3, 2, [(3, 1), (6, 2), (8, 3)], "N (Numarul de pagini) trebuie sa fie intre 1 si 1000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_3(self):
        # N > 1000
        N, M, K, intervals, expected = (
        1001, 3, 2, [(3, 1), (6, 2), (8, 3)], "N (Numarul de pagini) trebuie sa fie intre 1 si 1000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_4(self):
        # M < 1
        N, M, K, intervals, expected = (
        5, 0, 2, [(3, 1), (6, 2), (8, 3)], "M (Numarul de intervale) trebuie sa fie intre 1 si 10000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_5(self):
        # M > 10000
        N, M, K, intervals, expected = (
        5, 10001, 2, [(i, i) for i in range(1, 10002)], "M (Numarul de intervale) trebuie sa fie intre 1 si 10000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_6(self):
        # K < 1
        N, M, K, intervals, expected = (
        5, 3, 0, [(3, 1), (6, 2), (8, 3)], "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_7(self):
        # K > 1000
        N, M, K, intervals, expected = (
        5, 3, 1001, [(3, 1), (6, 2), (8, 3)], "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_8(self):
        # mi < 1
        N, M, K, intervals, expected = (
        5, 3, 2, [(0, 1), (6, 2), (8, 3)], "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_9(self):
        # mi > 100 000
        N, M, K, intervals, expected = (5, 3, 2, [(100001, 1), (6, 2), (8, 3)],
                                        "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_10(self):
        # ci < 1
        N, M, K, intervals, expected = (
        5, 3, 2, [(3, 0), (6, 2), (8, 3)], "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_11(self):
        # ci > 10 000
        N, M, K, intervals, expected = (
        5, 3, 2, [(3, 10001), (6, 2), (8, 3)], "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_12(self):
        # numarul de perechi (mi, ci) nu este M
        N, M, K, intervals, expected = (5, 3, 2, [(3, 1), (6, 2)], "Numarul de perechi (mi, ci) trebuie sa fie M")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()