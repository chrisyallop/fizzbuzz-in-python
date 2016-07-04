import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzBuzz = FizzBuzz()

    def test_100_entries_are_printed(self):
        sequence = self.fizzBuzz.generate()
        self.assertEqual(range(1, 101), sequence)
        self.assertEqual(1, sequence[0])
        self.assertEqual(100, sequence[-1])

if __name__ == '__main__':
    unittest.main()
