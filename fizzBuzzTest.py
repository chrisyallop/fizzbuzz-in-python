import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fizzBuzz = FizzBuzz()

    def test_100_entries_are_printed(self):
        fb = self.fizzBuzz.generate()
        self.assertEqual(100, len(fb))
        self.assertEqual(1, fb[0])
        self.assertEqual(98, fb[-3])

    def test_multiples_of_three_print_fizz(self):
        fb = self.fizzBuzz.generate()

        for i in range(2,101,3):
            if (i+1) % 5 != 0:
                self.assertEqual('Fizz', fb[i])

    def test_multiples_of_five_print_buzz(self):
        fb = self.fizzBuzz.generate()

        for i in range(4,101,5):
            if (i+1) % 3 != 0:
                self.assertEqual('Buzz', fb[i])

    def test_multiples_of_three_and_five_print_fizzbuzz(self):
        fb = self.fizzBuzz.generate()

        for i in range(4,101,5):
            if (i+1) % 3 == 0:
                self.assertEqual('FizzBuzz', fb[i])

if __name__ == '__main__':
    unittest.main()
