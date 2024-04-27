import unittest
from src.lab3 import sudoku


class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        values = [1, 2, 3, 4]
        needed_groups = [[1, 2], [3, 4]]
        actual_groups = sudoku.group(values, 2)
        self.assertEqual(needed_groups, actual_groups)

        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        needed_groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        actual_groups = sudoku.group(values, 3)
        self.assertEqual(needed_groups, actual_groups)

if __name__ == '__main__':
    unittest.main()