import pygame
from pygame import Vector2
from src.DrawDelegates.SpriteFactory import SpriteFactory
from src.ThirdParty.GameFramework import Sprite

class SpriteFactoryPygame(SpriteFactory):
    def get_field_sprite(self, cell_size: Vector2):
        sprite = Sprite("images/cell.png")
        sprite.set_size(cell_size)
        return sprite
    def get_head_sprite(self, cell_size: Vector2):
        sprite = Sprite("images/head.png")
        sprite.set_size(cell_size)
        return sprite

    def get_body_sprite(self, cell_size: Vector2):
        sprite = Sprite("images/body.png")
        sprite.set_size(cell_size)
        return sprite

    def get_tail_sprite(self, cell_size: Vector2):
        sprite = Sprite("images/tail.png")
        sprite.set_size(cell_size)
        return sprite

    def get_turn_sprite(self, cell_size: Vector2):
        sprite = Sprite("images/turn.png")
        sprite.set_size(cell_size)
        return sprite

    def get_bonus_sprite(self, cell_size: Vector2):
        sprite = Sprite("images/bonus.png")
        sprite.set_size(cell_size)
        return sprite
