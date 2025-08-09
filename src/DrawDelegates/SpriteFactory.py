import os

from pygame import Vector2
import re
from src.ThirdParty.GameFramework import Sprite

class SnakeSprite(Sprite):
    def __init__(self, path: str):
        super().__init__(path)
        self.orientation : Vector2 = SnakeSprite.__extract_orientation(path)

    @staticmethod
    def __extract_orientation(path: str):
        r = re.compile(r'{(-*\d)\s*,\s*(-*\d)}')
        x,y = r.match(path).groups()
        return Vector2(int(x), int(y))

    @staticmethod
    def extract_bare_name(path: str):
        return path.split('{')[0].strip()

class SpriteFactory:
    def __init__(self):
        self.sprite_list = {}

    def init(self, sprites_path, cell_size):
        self.load_sprites(sprites_path)
        self.set_sizes(cell_size)

    def load_sprites(self, sprites_path):
        for file in os.listdir(sprites_path):
            full_path = os.path.join(sprites_path, file)
            key = SnakeSprite.extract_bare_name(file)
            self.sprite_list[key] = Sprite(full_path)

    def set_sizes(self, cell_size):
        for value in self.sprite_list.values():
            value.set_size(cell_size)

    def get_sprite(self, sprite_name):
        return self.sprite_list[sprite_name]

SPRITE_FACTORY = SpriteFactory()
