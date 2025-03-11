from cell import Cell
from time import time
import random

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
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        self._cells = []

        self._create_cells()

        if seed is not None:
            random.seed(seed)

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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            # left
            if i > 0 and not self._cells[i - 1][j].visited:                
                possible_directions.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:                
                possible_directions.append((i + 1, j))
            # top
            if j > 0 and not self._cells[i][j - 1].visited:                
                possible_directions.append((i, j - 1))   
            # bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:                
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(possible_directions))
            to_visit = possible_directions[direction]
            
            # left
            if to_visit[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # right
            if to_visit[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # top
            if to_visit[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # bottom
            if to_visit[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            self._break_walls_r(to_visit[0], to_visit[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                