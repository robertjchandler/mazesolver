from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    c1 = Cell(Point(0, 0), Point(50, 50), True, True, True, True)
    win.draw_cell(c1, "black")
    c2 = Cell(Point(50, 50), Point(100, 100), True, True, True, False)
    win.draw_cell(c2, "black")
    c3 = Cell(Point(100, 100), Point(150, 150), True, True, False, True)
    win.draw_cell(c3, "black")
    c4 = Cell(Point(150, 150), Point(200, 200), True, False, True, True)
    win.draw_cell(c4, "black")
    c5 = Cell(Point(200, 200), Point(250, 250), False, True, True, True)
    win.draw_cell(c5, "black")
    win.wait_for_close()
    
main()
