from dataclasses import dataclass

from pygame import Vector2

from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.Patterns.Visitor import Visitable
from src.ThirdParty.GameFramework import Sprite



@dataclass
class Segment:
    type: str
    pos: Vector2
    dir: Vector2

class CollisionException(Exception):
    pass


class Snake(Visitable):
    def __init__(self, start_pos: Vector2):
        self.body = [start_pos.copy()]
        self.grow_pending = 0
        self.last_direction = Vector2(1, 0)
        self.__seg_names = ["head", "body", "tail"]

    def move(self, direction: Vector2):
        new_head = self.body[0] + direction
        if self.check_collision(new_head):
            raise CollisionException("Snake collided with itself")
        self.last_direction = direction
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def check_collision(self, head_pos: Vector2) -> bool:
        for segment in self.body[2:]:
            if head_pos == segment:
                return True
        return False

    def grow(self):
        self.grow_pending += 1


    def get_positions(self):
        return self.body

    def generate_segments(self):
        seg_names = {0: "head", len(self.body) - 1: "tail"}
        segments = []
        n = len(self.body)
        for i, pos in enumerate(self.body):
            cur_seg_name = seg_names.get(i, "body")
            offset = 1 - 2 * int(i < n - 1)
            neighbor_index = i + offset
            if 0 <= neighbor_index < n:
                cur_seg_dir = self.body[i] - self.body[neighbor_index]
            else:
                cur_seg_dir = Vector2(0, 0)
            segments.append(Segment(cur_seg_name, pos, cur_seg_dir))
        return segments

