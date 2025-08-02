from pygame import Vector2
import random

class Bonus:
    def __init__(self, field_size: int):
        self.position = self._generate_position(field_size)
    def _generate_position(self, field_size: int):
        return Vector2(random.randint(0, field_size-1), random.randint(0, field_size-1))
    def respawn(self, field_size: int):
        self.position = self._generate_position(field_size)
    def get_position(self):
        return self.position
