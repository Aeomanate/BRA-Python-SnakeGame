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

    @accept.register
    def _(self, snake: Snake):
        segments = snake.generate_segments()
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
            sprite = SPRITE_FACTORY.get_sprite('head')
            angle = vector_to_angle(seg.dir)
            sprite.draw(pos, angle)
            return

        for i, seg in enumerate(segments):
            sprite = SPRITE_FACTORY.get_sprite(seg.type)
            pos = Vector2(seg.pos.x * cell_size.x, seg.pos.y * cell_size.y)
            angle = vector_to_angle(seg.dir_in) if seg.dir_in == seg.dir_out else turn_angle(seg.dir_in, seg.dir_out)
            if seg.type == 'body' and n != 2:
                angle = vector_to_angle(seg.dir_in) if seg.dir_in == seg.dir_out else turn_angle(seg.dir_in, seg.dir_out)
            sprite.draw(pos, angle)

    @accept.register
    def _(self, bonus: Bonus):

        bonus_sprite = SPRITE_FACTORY.get_sprite('bonus')
        pos = Vector2(bonus.position.x * self.cell_size.x, bonus.position.y * self.cell_size.y)
        bonus_sprite.draw(pos)


