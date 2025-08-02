from dataclasses import dataclass

from pygame import Vector2

from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.Patterns.Visitor import Visitable
from src.ThirdParty.GameFramework import Sprite

@dataclass
class DirInOut:
    dir_in: Vector2
    dir_out: Vector2

@dataclass
class Segment:
    type: str
    pos: Vector2
    dir: Vector2 | DirInOut

class CollisionException(Exception):
    pass


class Snake(Visitable):
    def __init__(self, start_pos: Vector2):
        self.body = [start_pos.copy()]
        self.grow_pending = 0
        self.last_direction = Vector2(1, 0)

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

    def get_segments_with_directions(self):
        segments = []
        n = len(self.body)
        for i, pos in enumerate(self.body):
            if i == 0:
                direction = self.body[0] - self.body[1] if n > 1 else self.last_direction
                segments.append(Segment('head', pos, direction))
            elif i == n - 1:
                direction = self.body[-2] - self.body[-1] if n > 1 else Vector2(0, 0)
                segments.append(Segment('tail', pos, direction))
            else:
                prev_dir = self.body[i-1] - pos
                next_dir = pos - self.body[i+1]
                segments.append(Segment('head', pos, DirInOut(next_dir, prev_dir)))
        return segments

