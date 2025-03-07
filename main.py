from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    d = Cell(win)
    d.has_right_wall = False
    d.draw(125, 125, 200, 200)

    c.draw_move(d)

    e = Cell(win)
    e.has_bottom_wall = False
    e.draw(225, 225, 250, 250)

    d.draw_move(e, undo=True)

    f = Cell(win)
    f.has_top_wall = False
    f.draw(300, 300, 500, 500)

    e.draw_move(f)

    win.wait_for_close()
    
main()
