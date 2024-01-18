# Christopher Buchanan
# Pledge: "I pledge my honor that I abided by Stevens Honor System"
# CS115 Homework 4

import unittest

def pascal_row(n):
    """Outputs a list of elements found in a specific row of Pascal's Triangle.
    Takes a singular integer as an input (row number)"""
    if n < 0:
        return []

    def binomial_coefficient(k):
        """Helper Function: Does the math to find the elements in for a specific row
        in Pascal's Triangle"""
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(k - 1) * (n - k + 1) // k

    return list(map(binomial_coefficient, range(n + 1)))
    
def pascal_triangle(n):
    """Outputs a list of each step found up to a specific row of Pascal's Triangle. 
    Takes a singular integer as an input (row number)"""

    if n <= 0:
        return [[1]]

    def next_Row(prev_row):
        """Helper Function: Creates the next row of Pascal's triangle to add to the
        outputted list"""
        if not prev_row:
            return [1]
        return [1] + list(map(lambda i: prev_row[i] + prev_row[i + 1], range(len(prev_row) - 1))) + [1]

    def generate_triangle(rows, triangle=[]):
        """Helper Function: Builds the list of the traingle with the help from next_Row"""
        if rows == 0:
            return triangle
        next_row = next_Row(triangle[-1] if triangle else [])
        return generate_triangle(rows - 1, triangle + [next_row])
    
    return generate_triangle(n+1)

class test_pascal_row(unittest.TestCase):
    def test_pascal_row01(self):
        # Test Pascal's Row with n = 0
        expected_result = [1]
        self.assertEqual(pascal_row(0), expected_result)
    def test_pascal_row02(self):
        # Test Pascal's Row with n = 1
        expected_result = [1, 1]
        self.assertEqual(pascal_row(1), expected_result)
    def test_pascal_row03(self):
        # Test Pascal's Row with n = 2
        expected_result = [1, 2, 1]
        self.assertEqual(pascal_row(2), expected_result)
    def test_pascal_row04(self):
        # Test Pascal's Row with n = 3
        expected_result = [1, 3, 3, 1]
        self.assertEqual(pascal_row(3), expected_result)

class test_pascal_triangle(unittest.TestCase):
    def test_pascal_triangle01(self):
        # Test Pascal's Triangle with n = 0
        expected_result = [[1]]
        self.assertEqual(pascal_triangle(0), expected_result)
    def test_pascal_triangle02(self):
        # Test Pascal's Triangle with n = 1
        expected_result = [[1], [1, 1]]
        self.assertEqual(pascal_triangle(1), expected_result)
    def test_pascal_triangle03(self):
        # Test Pascal's Triangle with n = 2
        expected_result = [[1], [1, 1], [1, 2, 1]]
        self.assertEqual(pascal_triangle(2), expected_result)
    def test_pascal_triangle04(self):
        # Test Pascal's Triangle with n = 3
        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        self.assertEqual(pascal_triangle(3), expected_result)

if __name__ == "__main__":
    unittest.main()
