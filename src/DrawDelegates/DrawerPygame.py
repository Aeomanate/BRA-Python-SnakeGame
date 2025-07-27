
import pygame
from pygame import Vector2
from src.DrawDelegates.Drawer import Drawer
from src.ThirdParty.GameFramework import Sprite


from src.DrawDelegates.SpriteFactoryPygame import SpriteFactoryPygame

class DrawerPygame(Drawer):
    def __init__(self):
        self.sprite_factory = SpriteFactoryPygame()

    def draw_field(self, field_size: int, cell_size: Vector2, font):
        surface = pygame.display.get_surface()
        cell_color = (200, 200, 200)
        for y in range(field_size):
            for x in range(field_size):
                rect = pygame.Rect(x * cell_size.x, y * cell_size.y, cell_size.x, cell_size.y)
                pygame.draw.rect(surface, cell_color, rect)
                text_str = f"{x},{y}"
                text = font.render(text_str, True, (128, 128, 128))
                surface.blit(text, rect.topleft)

    def draw_snake(self, segments, cell_size: Vector2):
        import math
        surface = pygame.display.get_surface()

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
            segment = segments[0]
            pos = Vector2(segment['pos'].x * cell_size.x, segment['pos'].y * cell_size.y)
            sprite = self.sprite_factory.get_head_sprite(cell_size)
            angle = vector_to_angle(segment['dir'])
            sprite.draw(pos, angle)
            return

        for i, segment in enumerate(segments):
            pos = Vector2(segment['pos'].x * cell_size.x, segment['pos'].y * cell_size.y)
            if segment['type'] == 'head':
                sprite = self.sprite_factory.get_head_sprite(cell_size)
                angle = vector_to_angle(segment['dir'])
            elif segment['type'] == 'tail':
                sprite = self.sprite_factory.get_tail_sprite(cell_size)
                angle = vector_to_angle(segment['dir'])
            elif segment['type'] == 'body':
                if n == 2:
                    continue
                if segment['dir_in'] == segment['dir_out']:
                    sprite = self.sprite_factory.get_body_sprite(cell_size)
                    angle = vector_to_angle(segment['dir_in'])
                else:
                    sprite = self.sprite_factory.get_turn_sprite(cell_size)
                    angle = turn_angle(segment['dir_in'], segment['dir_out'])
            else:
                continue
            sprite.draw(pos, angle)

    def draw_bonus(self, position: Vector2, cell_size: Vector2):
        bonus_sprite = self.sprite_factory.get_bonus_sprite(cell_size)
        pos = Vector2(position.x * cell_size.x, position.y * cell_size.y)
        bonus_sprite.draw(pos)
