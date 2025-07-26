from pygame import Vector2


class Field:
    def __init__(self, window_size_px, cells):
        self.FIELD_SIZE = 11
        self.cell_size = Vector2(640 // self.FIELD_SIZE)
        self.head_pos = (5, 5)
        self.window_size: Vector2 = window_size_px
        self.cells: int = cells