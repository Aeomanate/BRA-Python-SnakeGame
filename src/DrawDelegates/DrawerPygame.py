from functools import singledispatchmethod

import math
import pygame
from pygame import Vector2
from src.DrawDelegates.Font import FONT
from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.Patterns.Visitor import Visitor
from src.Simulation.Bonus import Bonus
from src.Simulation.Field import Field
from src.Simulation.Snake import Snake
from src.ThirdParty.GameFramework import Sprite


class DrawerPygame(Visitor):
    def __init__(self, cell_size):
        self.cell_size = cell_size

    @singledispatchmethod
    def accept(self, obj):
        raise NotImplementedError(f"Object of type {type(obj)} is not supported")

    @accept.register
    def _(self, field: Field):
        surface = pygame.display.get_surface()
        cell_color = (200, 200, 200)
        for y in range(field.cells_nxn):
            for x in range(field.cells_nxn):
                cell_size = field.cell_size
                rect = pygame.Rect(x * cell_size.x, y * cell_size.y, cell_size.x, cell_size.y)
                pygame.draw.rect(surface, cell_color, rect)
                text_str = f"{x},{y}"
                text = FONT.font.render(text_str, True, (128, 128, 128))
                surface.blit(text, rect.topleft)

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

    @accept.register
    def _(self, snake: Snake):
        segments = snake.get_segments_with_directions()
        cell_size = self.cell_size

        def vector_to_angle(vec):
            if vec.length() == 0:
                return 0.0
            return math.atan2(vec.x, -vec.y)

        def turn_angle(dir_in, dir_out):
            base_angle = vector_to_angle(dir_in)
            if dir_in.x * dir_out.y - dir_in.y * dir_out.x > 0:
                return base_angle - math.pi / 2
            else:
                return base_angle

        n = len(segments)
        if n == 1:
            seg = segments[0]
            pos = Vector2(seg.pos.x * cell_size.x, seg.pos.y * cell_size.y)
            sprite = SPRITE_FACTORY.get_head_sprite(cell_size)
            angle = vector_to_angle(seg.dir)
            sprite.draw(pos, angle)
            return

        for i, seg in enumerate(segments):

            sprite = SPRITE_FACTORY.get_sprite(seg.type)
            angle = vector_to_angle(seg.dir_in) if seg.dir_in == seg.dir_out else turn_angle(seg.dir_in, seg.dir_out)

            match seg.type:
                case ('head' | 'tail' | 'body') if n != 2:
                    if seg.type == 'body':
                        angle = vector_to_angle(seg.dir_in) if seg.dir_in == seg.dir_out else turn_angle(seg.dir_in,
                                                                                                         seg.dir_out)
                case 'body':
                    continue

                case _:
                    continue

            if and n != 2:
                sprite = SPRITE_FACTORY.get_sprite(seg.type)
                if seg.type == 'body':
                    angle = vector_to_angle(seg.dir_in) if seg.dir_in == seg.dir_out else turn_angle(seg.dir_in, seg.dir_out)
                else:
                    angle = vector_to_angle(seg.dir)

            pos = Vector2(seg.pos.x * cell_size.x, seg.pos.y * cell_size.y)
            if :
                sprite = SPRITE_FACTORY.get_sprite(seg.type)
                angle = vector_to_angle(seg.dir)
            elif seg.type == 'body':
                if n == 2:
                    continue
                if seg.dir_in == seg.dir_out:
                    sprite = SPRITE_FACTORY.get_sprite(seg.type)
                    angle = vector_to_angle(seg.dir_in)
                else:
                    sprite = SPRITE_FACTORY.get_sprite(seg.type)
                    angle = turn_angle(seg.dir_in, seg.dir_out)
            else:
                continue
            sprite.draw(pos, angle)

    @accept.register
    def _(self, bonus: Bonus):

        bonus_sprite = SPRITE_FACTORY.get_sprite('bonus')
        pos = Vector2(bonus.position.x * self.cell_size.x, bonus.position.y * self.cell_size.y)
        bonus_sprite.draw(pos)


