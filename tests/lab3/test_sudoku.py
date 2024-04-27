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

    def test_get_row(self):
        puzzle = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        pos = (0, 0)
        needed_row = ['1', '2', '.']
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(needed_row, actual_row)

        puzzle = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        pos = (1, 0)
        needed_row = ['4', '.', '6']
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(needed_row, actual_row)

        puzzle = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        pos = (2, 0)
        needed_row = ['.', '8', '9']
        actual_row = sudoku.get_row(puzzle, pos)
        self.assertEqual(needed_row, actual_row)

    def test_get_col(self):
        puzzle = [['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]
        pos = (0, 0)
        needed_col = ['1', '4', '7']
        actual_col = sudoku.get_col(puzzle, pos)
        self.assertEqual(needed_col, actual_col)

        puzzle = [['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]
        pos = (0, 1)
        needed_col = ['2', '.', '8']
        actual_col = sudoku.get_col(puzzle, pos)
        self.assertEqual(needed_col, actual_col)

        puzzle = [['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]
        pos = (0, 2)
        needed_col = ['3', '6', '9']
        actual_col = sudoku.get_col(puzzle, pos)
        self.assertEqual(needed_col, actual_col)

if __name__ == '__main__':
    unittest.main()