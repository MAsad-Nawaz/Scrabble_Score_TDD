import unittest
from scrabble_score import scrabble_score, is_valid_word, load_dictionary

class TestScrabbleScore(unittest.TestCase):
    def setUp(self):
        # Set up a dictionary for testing
        self.dictionary = load_dictionary()

    def test_scrabble_score(self):
        # Test known Scrabble scores
        self.assertEqual(scrabble_score("apple"), 9)
        self.assertEqual(scrabble_score("banana"), 8)
        self.assertEqual(scrabble_score("cabbage"), 14)

    def test_is_valid_word(self):
        # Test valid words
        if self.dictionary:
            self.assertTrue(is_valid_word("apple", self.dictionary))
            self.assertTrue(is_valid_word("banana", self.dictionary))
            # Test invalid word
            self.assertFalse(is_valid_word("notaword", self.dictionary))

if __name__ == '__main__':
    unittest.main()
