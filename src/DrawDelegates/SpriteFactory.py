import os

from src.ThirdParty.GameFramework import Sprite


class SpriteFactory:
    def __init__(self):
        self.sprite_list = {}

    def init(self, sprites_path):
        self.load_sprites(sprites_path)

    def load_sprites(self, sprites_path):
        for file in os.listdir(sprites_path):
            full_path = os.path.join(sprites_path, file)
            key = file.split('.')[0]

            self.sprite_list[key] = Sprite(full_path)

    def get_sprite(self, sprite_name):
        return self.sprite_list[sprite_name]

SPRITE_FACTORY = SpriteFactory()
