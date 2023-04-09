import unittest
from main import min_cost_to_buy_stamps
# from main2 import min_cost_to_buy_stamps
"""
Clasele intrarilor:
    1) N:
    N_1 = 1 # valoarea minima valida
    N_2 = 1000 # valoarea maxima valida
    N_3 = 2 # valoarea valida aproape de minimul intervalului 
    N_4 = 999 # valoarea valida aproape de maximul intervalului
    N_5 = 0 # valoarea maxima invalida de langa limita inferioara a intervalului de valori valide
    N_6 = 1001 # valoarea minima invalida de langa limita superioara a intervalului de valori valide

    2)  M:
    M_1 = 1 # valoarea minima valida
    M_2 = 10 000 # valoarea maxima valida
    M_3 = 2 # valoarea valida aproape de minimul intervalului 
    M_4 = 9999 # valoarea valida aproape de maximul intervalului
    M_5 = 0 # valoarea maxima invalida de langa limita inferioara a intervalului de valori valide
    M_6 = 10 001 # valoarea minima invalida de langa limita superioara a intervalului de valori valide


    3)  K:
    K_1 = 1 # valoarea minima valida
    K_2 = 1000 # valoarea maxima valida
    K_3 = 2 # valoarea valida aproape de minimul intervalului 
    K_4 = 999 # valoarea valida aproape de maximul intervalului
    K_5 = 0 # valoarea maxima invalida de langa limita inferioara a intervalului de valori valide
    K_6 = 10 001 # valoarea minima invalida de langa limita superioara a intervalului de valori valide
    4) mi:
        mi_1 = 1 # valoarea minima valida
        mi_2 = 99 999 # valoarea maxima valida
        mi_3 = 2 # valoarea valida aproape de minimul intervalului 
        mi_4 = 99 998 # valoarea valida aproape de maximul intervalului
        mi_5 = 0 # valoarea maxima invalida de langa limita inferioara a intervalului de valori valide
        mi_6 = 100 001 # valoarea minima invalida de langa limita superioara a intervalului de valori valide

    5) ci:
        ci_1 = 1 # valoarea minima valida
        ci_2 = 9 999 # valoarea maxima valida
        ci_3 = 2 # valoarea valida aproape de minimul intervalului 
        ci_4 = 9 998 # valoarea valida aproape de maximul intervalului
        ci_5 = 0 # valoarea maxima invalida de langa limita inferioara a intervalului de valori valide
        ci_6 = 10 001 # valoarea minima invalida de langa limita superioara a intervalului de valori valide

    ----------------------------------------------------------------    
    Clase iesiri:
    i_1 = Numar - Solutia dorita (toate datele de intrare sunt valide)
    i_2 = "N (Numarul de pagini) trebuie sa fie intre 1 si 1000"
    i_3 = "M (Numarul de intervale) trebuie sa fie intre 1 si 10000"
    i_4 = "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000"
    i_5 = "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 10000)"
    i_6 = "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)"

    ----------------------------------------------------------------
    Clase de echivalenta finala:
    C_1 = {N, M, K, (mi, ci) | N in N_1, M in M_1, K in K_1, mi in mi_1, ci in ci_1 si iesirea i_1}
    C_2 = {N, M, K, (mi, ci) | N in N_2, M in M_2, K in K_2, mi in mi_2, ci in ci_2 si iesirea i_1}
    C_3 = {N, M, K, (mi, ci) | N in N_3, M in M_3, K in K_3, mi in mi_3, ci in ci_3 si iesirea i_1}
    C_4 = {N, M, K, (mi, ci) | N in N_4, M in M_4, K in K_4, mi in mi_4, ci in ci_4 si iesirea i_1}
    C_5 = {N, M, K, (mi, ci) | N in N_5, M, K, mi, ci - toate valide si iesirea i_2}
    C_6 = {N, M, K, (mi, ci) | N in N_6, M, K, mi, ci - toate valide si iesirea i_2}
    C_7 = {N, M, K, (mi, ci) | M in M_5, N, K, mi, ci - toate valide si iesirea i_3}
    C_8 = {N, M, K, (mi, ci) | M in M_6, N, K, mi, ci - toate valide si iesirea i_3}
    C_9 = {N, M, K, (mi, ci) | K in M_5, N, M, mi, ci - toate valide si iesirea i_4}
    C_10 = {N, M, K, (mi, ci) | K in M_6, N, M, mi, ci - toate valide si iesirea i_4}
    C_11 = {N, M, K, (mi, ci) | mi in mi_5, N, M, K, ci - toate valide si iesirea i_5}
    C_12 = {N, M, K, (mi, ci) | mi in mi_6, N, M, K, ci - toate valide si iesirea i_5}
    C_13 = {N, M, K, (mi, ci) | ci in ci_5, N, M, K, mi - toate valide si iesirea i_6}
    C_14 = {N, M, K, (mi, ci) | ci in ci_6, N, M, K, mi - toate valide si iesirea i_6}

"""

class TestStampMinCost(unittest.TestCase):
    def test_C_1(self):
        N, M, K, intervals, expected = (1, 1, 1, [(1, 1)], 1)
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_2(self):
        N, M, K, intervals, expected = (1000, 10, 1000, [(1000 * i, 1) for i in range(1, 11)], 1)
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_3(self):
        N, M, K, intervals, expected = (2, 2, 2, [(2, 1), (3, 2)], 1)
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_4(self):
        N, M, K, intervals, expected = (1000, 5, 1000, [(1000 * i, 1) for i in range(1, 6)], 1)
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_5(self):
        N, M, K, intervals, expected = (0, 3, 2, [(3, 1), (6, 2), (8, 3)], "N (Numarul de pagini) trebuie sa fie intre 1 si 1000")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_6(self):
        N, M, K, intervals, expected = (1001, 3, 2, [(3, 1), (6, 2), (8, 3)], "N (Numarul de pagini) trebuie sa fie intre 1 si 1000")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_7(self):
        N, M, K, intervals, expected = (5, 0, 2, [(3, 1), (6, 2), (8, 3)], "M (Numarul de intervale) trebuie sa fie intre 1 si 10000")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_8(self):
        N, M, K, intervals, expected = (5, 10001, 2, [(3, 1), (6, 2), (8, 3)], "M (Numarul de intervale) trebuie sa fie intre 1 si 10000")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_9(self):
        N, M, K, intervals, expected = (5, 3, 0, [(3, 1), (6, 2), (8, 3)], "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_10(self):
        N, M, K, intervals, expected = (5, 3, 1001, [(3, 1), (6, 2), (8, 3)], "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_11(self):
        N, M, K, intervals, expected = (5, 3, 2, [(0, 1), (6, 2), (8, 3)], "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_12(self):
        N, M, K, intervals, expected =  (5, 3, 2, [(100001, 1), (6, 2), (8, 3)], "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_13(self):
        N, M, K, intervals, expected = (5, 3, 2, [(3, 0), (6, 2), (8, 3)], "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)

    def test_C_14(self):
        N, M, K, intervals, expected =(5, 3, 2, [(3, 10001), (6, 2), (8, 3)], "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)")
        self.assertEqual(min_cost_to_buy_stamps((N, M, K, intervals)), expected)


if __name__ == '__main__':
    unittest.main()