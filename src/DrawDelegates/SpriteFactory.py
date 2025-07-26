import os

from src.ThirdParty.GameFramework import Sprite


class SpriteFactory:
    def __init__(self):
        self.sprite_list = {}

    def init(self, sprites_path, cell_size):
        self.load_sprites(sprites_path)
        self.set_sizes(cell_size)

    def load_sprites(self, sprites_path):
        for file in os.listdir(sprites_path):
            full_path = os.path.join(sprites_path, file)
            key = file.split('.')[0]

            self.sprite_list[key] = Sprite(full_path)

    def set_sizes(self, cell_size):
        for value in self.sprite_list.values():
            value.set_size(cell_size)

    def get_sprite(self, sprite_name):
        return self.sprite_list[sprite_name]

SPRITE_FACTORY = SpriteFactory()
