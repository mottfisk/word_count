import main
import unittest

class TestCountWords(unittest.TestCase):
    def test_one_word(self):
        assert main.count_words('hi') == 1

    def test_two_words(self):
        assert main.count_words('hi everybody') == 2

    def test_three_words(self):
        assert main.count_words('i dont understand') == 3
