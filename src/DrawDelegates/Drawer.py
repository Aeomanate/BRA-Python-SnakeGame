from pygame import Vector2


class Drawer:
    def draw_field(self, field_size: int, cell_size: Vector2, font):
        raise NotImplementedError

    def draw_snake(self, positions: list[Vector2], cell_size: Vector2):
        raise NotImplementedError

    def draw_bonus(self, position: Vector2, cell_size: Vector2):
        raise NotImplementedError
