import unittest
from pkg.calculator import Calculator
from functions.get_files_info import get_files_info

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("3 + 5"), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("3 * 4"), 12)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("10 / 2"), 5)

    def test_nested_expression(self):
        self.assertEqual(self.calculator.evaluate("3 * 4 + 5"), 17)

    def test_complex_expression(self):
        self.assertEqual(self.calculator.evaluate("2 * 3 - 8 / 2 + 5"), 7)

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate(""))

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

import os

def run_get_files_info_tests():
    print("\nManual Tests for get_files_info:")
    
    working_dir = os.path.abspath("calculator")
    
    print("\nTest 1: get_files_info('calculator', '.')")
    print(get_files_info(working_dir, "."))  # Should list main.py, render.py, calculator.py, etc.

    print("\nTest 2: get_files_info('calculator', 'tests.py')")
    print(get_files_info(working_dir, "tests.py"))  # Should error: not a directory

    print("\nTest 3: get_files_info('calculator', '/bin')")
    print(get_files_info(working_dir, "/bin"))  # Should error: outside working directory

    print("\nTest 4: get_files_info('calculator', '../')")
    print(get_files_info(working_dir, "../"))  # Should error: outside working directory


if __name__ == "__main__":
    unittest.main(exit=False)  # Prevents immediate exit after tests
    run_get_files_info_tests()
