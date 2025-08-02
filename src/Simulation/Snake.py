
from pygame import Vector2

from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.ThirdParty.GameFramework import Sprite


class CollisionException(Exception):
    pass


class Snake:
    def __init__(self, start_pos: Vector2, cell_size: Vector2):
        self.body = [start_pos.copy()]
        self.cell_size = cell_size
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
                segments.append({
                    'type': 'head',
                    'pos': pos,
                    'dir': direction
                })
            elif i == n - 1:
                direction = self.body[-2] - self.body[-1] if n > 1 else Vector2(0, 0)
                segments.append({
                    'type': 'tail',
                    'pos': pos,
                    'dir': direction
                })
            else:
                prev_dir = self.body[i-1] - pos
                next_dir = pos - self.body[i+1]
                segments.append({
                    'type': 'body',
                    'pos': pos,
                    'dir_in': prev_dir,
                    'dir_out': next_dir
                })
        return segments

    def draw(self, cell_size) -> bool:
        for index, peace in enumerate(self.body):
            match index + 1:
                case 1:
                    SPRITE_FACTORY.get_sprite('head').draw(Vector2(peace.x * cell_size.x, peace.y * cell_size.y))
                case len(self.body):
                    SPRITE_FACTORY.get_sprite('tail').draw(Vector2(peace.x * cell_size.x, peace.y * cell_size.y))
                case _:
                    SPRITE_FACTORY.get_sprite('body').draw(Vector2(peace.x * cell_size.x, peace.y * cell_size.y))

        return False

