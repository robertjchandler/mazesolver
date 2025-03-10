from cell import Cell
from time import time
import random
random.seed(a=None)

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(win=self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        entrance.draw(entrance._x1, entrance._y1, entrance._x2, entrance._y2)
        exit = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit.has_bottom_wall = False
        exit.draw(exit._x1, exit._y1, exit._x2, exit._y2)

    def _break_walls_r(self, i=0, j=0):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if i < current_cell._num_cols and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j < current_cell._num_rows and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            if len(possible_directions) == 0:
                current_cell.draw(current_cell._x1, current_cell._y1, current_cell._x2, current_cell._y2)
                break
            direction = random.randrange(len(possible_directions))
            