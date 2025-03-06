class Cell:
    def __init__(self, p1, p2, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
        #self.__win

    def draw(self, canvas, fill_color="black"):
        if self.has_left_wall:
            canvas.create_line(
                self.__x1, self.__y1, self.__x1, self.__y2, fill=fill_color, width=2
            )
        if self.has_top_wall:
            canvas.create_line(
                self.__x1, self.__y2, self.__x2, self.__y2, fill=fill_color, width=2
            )
        if self.has_right_wall:
            canvas.create_line(
                self.__x2, self.__y2, self.__x2, self.__y1, fill=fill_color, width=2
            )
        if self.has_bottom_wall:
            canvas.create_line(
                self.__x2, self.__y1, self.__x1, self.__y1, fill=fill_color, width=2
            )
