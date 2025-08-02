from pygame import Vector2

from src.Patterns.Visitor import Visitable


class Field(Visitable):
    def __init__(self, window_size_px, cells_nxn):
        self.FIELD_SIZE = 11
        self.cell_size = Vector2(640 // self.FIELD_SIZE)
        self.window_size: Vector2 = window_size_px
        self.cells_nxn: int = cells_nxn

