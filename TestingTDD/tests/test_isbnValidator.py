import unittest
from src.IsbnValidator import IsbnValidator

class test_IsbnValidator(unittest.TestCase):
    def test_verifier_si_isbn_est_valide(self):
        isbn_Validator = IsbnValidator()

        resultat = isbn_Validator.verifier_isbn(1491926309)

        self.assertTrue(resultat, "Le numero ISBN est valide")


    def test_verifier_si_isbn_est_invalide(self):
        isbn_Validator = IsbnValidator()

        resultat = isbn_Validator.verifier_isbn(1491926308)

        self.assertFalse(resultat, "Le numero ISBN est valide")


if __name__ == '__main__':
    unittest.main()