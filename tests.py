import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_sm(self):
        num_cols = 6
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_lg(self):
        num_cols = 24
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 24
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[m1._num_cols - 1][m1._num_rows - 1].has_bottom_wall)

    def test_reset_cells_visited(self):
        num_cols = 24
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                m1._cells[i][j].visited = True
        m1._reset_cells_visited()
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertFalse(m1._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()

    