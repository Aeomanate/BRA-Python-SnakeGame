import pygame
from pygame import Vector2

from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.ThirdParty.GameFramework import Sprite


class Snake:
    def __init__(self, head_pos: Vector2):
        self.body = [head_pos]
        self.head: Sprite | None = None

    def init(self, cell_size) -> bool:

        # self.head = Sprite("images/head.png")
        # self.head.set_size(cell_size)

        return True

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
