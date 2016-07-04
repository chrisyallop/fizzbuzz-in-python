import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello World", FizzBuzz.hello_world())

if __name__ == '__main__':
    unittest.main()
