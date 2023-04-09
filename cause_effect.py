import unittest
from main import min_cost_to_buy_stamps
# from main3 import min_cost_to_buy_stamps

"""
Clasele intrarilor: 
    - N (Numarul de pagini ale clasorului) 0 < N < 1001
    - M (Numarul de intervale de timbre) 0 < M < 10001
    - K (Lungimea maxima a unei subsecvente de timbre care poate fi luata din interval) 0 < K < 1001
    - (mi, ci) i <= M:   
        - mi (Marginea superioara a intervalului i) 0 < mi < 100 000, i <= M
        - ci (Costul intervalului i) 0 < ci < 10 000, i <= M
----------------------------------------------------------------
Cauze:
    1) Alegerea variabilei N
    2) Alegerea variabilei M
    3) Alegerea variabilei K
    4) Alegerea variabilei mi
    5) Alegerea variabilei ci
    6) Alegerea numarului total de intervale (ci, mi)
    
Efecte:
    1) Afisarea raspunsului (suma minima pe care copila trebuie sa o plateasca pentru a cumpara timbrele necesare)
    2) Afisarea mesajului de eroare: "N (Numarul de pagini) trebuie sa fie intre 1 si 1000"
    3) Afisarea mesajului de eroare: "M (Numarul de intervale) trebuie sa fie intre 1 si 10000"
    4) Afisarea mesajului de eroare: "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000"
    5) Afisarea mesajului de eroare: "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 10000)"
    6) Afisarea mesajului de eroare: "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)"
    7) Afisarea mesajului de eroare: "Numarul de perechi (mi, ci) trebuie sa fie M"
    
"""

class TestStampMinCost(unittest.TestCase):
    def test_C_1(self):
        # valid inputs
        N, M, K, intervals, expected = (10, 3, 5, [(10, 4), (20, 7), (30, 8)], 11)
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_2(self):
        # N invalid
        N, M, K, intervals, expected = (-1, 3, 5, [(10, 4), (20, 7), (30, 8)], "N (Numarul de pagini) trebuie sa fie intre 1 si 1000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_3(self):
        # M invalid
        N, M, K, intervals, expected = (10, 10001, 5, [(10, 4), (20, 7), (30, 8)], "M (Numarul de intervale) trebuie sa fie intre 1 si 10000")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_4(self):
        # K invalid
        N, M, K, intervals, expected =  (10, 3, 1001, [(10, 4), (20, 7), (30, 8)], "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000" )
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_5(self):
        # mi invalid
        N, M, K, intervals, expected =  (10, 3, 5, [(10, 4), (100001, 7), (30, 8)], "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_6(self):
        # ci invalid
        N, M, K, intervals, expected = (10, 3, 5, [(10, 4), (20, 10001), (30, 8)], "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)

    def test_C_7(self):
        # numarul de perechi (mi, ci) este invalid (Nu este M)
        N, M, K, intervals, expected = (10, 3, 5, [(10, 4), (20, 7)], "Numarul de perechi (mi, ci) trebuie sa fie M")
        result = min_cost_to_buy_stamps((N, M, K, intervals))
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()