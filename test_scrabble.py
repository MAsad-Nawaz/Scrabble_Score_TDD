import unittest
from your_module import scrabble_score, is_valid_word

class TestScrabbleScore(unittest.TestCase):
    def test_valid_scores(self):
        self.assertEqual(scrabble_score("apple"), 9)
        self.assertEqual(scrabble_score("banana"), 9)

    def test_invalid_word(self):
        self.assertFalse(is_valid_word("notaword", {"apple", "banana"}))
        self.assertTrue(is_valid_word("apple", {"apple", "banana"}))

if __name__ == '__main__':
    unittest.main()
