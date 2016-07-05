import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzBuzz = FizzBuzz()

    def test_100_entries_are_printed(self):
        sequence = self.fizzBuzz.generate()
        self.assertEqual(100, len(sequence))
        self.assertEqual(1, sequence[0])
        self.assertEqual(100, sequence[-1])

    def test_multiples_of_three_print_fizz(self):
        sequence = self.fizzBuzz.generate()
        self.assertEqual('Fizz', sequence[2])
        self.assertEqual('Fizz', sequence[5])
        for i in range(2,101,3):
            sequence[i] = 'Fizz'

if __name__ == '__main__':
    unittest.main()
