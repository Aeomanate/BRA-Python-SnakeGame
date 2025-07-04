import pygame

import GameFramework
from GameFramework import Framework, FRKey, Sprite


class MyGame(Framework):
    def __init__(self):
        self.font = None
        self.bonus = None
        self.head = None
        self.body = None
        self.FIELD_SIZE = 10
        self.cell_width = 640 // self.FIELD_SIZE
        self.cell_height = 640 // self.FIELD_SIZE
        self.head_x = 5
        self.head_y = 5

    def PreInit(self) -> tuple[int, int, bool]:
        pygame.font.init()
        return 640, 640, False


    def Init(self) -> bool:
        self.font = pygame.font.SysFont('Arial', 10)
        self.head = Sprite("images/head.png")
        self.head.set_size(self.cell_width, self.cell_height)
        return True

    def Tick(self) -> bool:
        self.draw_test_field()
        self.head.draw(self.head_x * self.cell_width, self.head_y * self.cell_height)
        return False

    def draw_test_field(self):
        surface = pygame.display.get_surface()
        for y in range(self.FIELD_SIZE):
            for x in range(self.FIELD_SIZE):
                color = (200, 200, 200) if (x + y) % 2 == 0 else (150, 150, 150)
                pygame.draw.rect(surface, color, (x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height))
                text = self.font.render(f'({x}, {y})', True, (0, 0, 0))
                surface.blit(text, (x * self.cell_width, y * self.cell_height))

    def onMouseMove(self, x: int, y: int, xrelative: int, yrelative: int) -> None:
        pass

    def onMouseButtonClick(self, button: GameFramework.FRMouseButton, isReleased: bool) -> None:
        pass

    def onKeyPressed(self, key: FRKey) -> None:
        match key:
            case FRKey.RIGHT:
                self.head_x += 1
            case FRKey.LEFT:
                self.head_x -= 1
            case FRKey.DOWN:
                self.head_y += 1
            case FRKey.UP:
                self.head_y -= 1

    def onKeyReleased(self, k: FRKey) -> None:
        pass

    def Close(self) -> None:
        pass

    def GetTitle(self) -> str:
        return "Snake Game"


if __name__ == "__main__":
    game = MyGame()
    GameFramework.run(game)
