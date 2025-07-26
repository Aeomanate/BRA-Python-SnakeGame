import pygame
from pygame import Vector2

from src.Simulation.Field import Field
from src.ThirdParty import GameFramework
from src.ThirdParty.GameFramework import Framework, Sprite, FRKey


class MyGame(Framework):
    def __init__(self):
        self.font = None
        self.head: Sprite | None = None
        self.window_size = Vector2(640, 640)
        self.field = Field(self.window_size, 11)
        # self.FIELD_SIZE = 11
        # self.cell_size = Vector2(self.window_size // self.FIELD_SIZE)
        self.head_pos = Vector2(5, 5)

    def PreInit(self) -> tuple[int, int, bool]:
        pygame.font.init()
        return int(self.window_size.x), int(self.window_size.y), False

    def Init(self) -> bool:
        self.font = pygame.font.SysFont('Arial', 10)
        self.head = Sprite("images/head.png")
        self.head.set_size(self.field.cell_size)
        return True

    def Tick(self) -> bool:
        self.draw_test_field()
        self.head.draw(Vector2(self.head_pos.x * self.field.cell_size.x, self.head_pos.y * self.field.cell_size.y))
        return False

    def draw_test_field(self):
        surface = pygame.display.get_surface()
        for y in range(self.field.FIELD_SIZE):
            for x in range(self.field.FIELD_SIZE):
                color = (200, 200, 200) if (x + y) % 2 == 0 else (150, 150, 150)
                pos = Vector2(self.field.cell_size.x * x, self.field.cell_size.y * y)
                pygame.draw.rect(surface, color,(pos, self.field.cell_size))
                text = self.font.render(f'({x}, {y})', True, (0, 0, 0))
                surface.blit(text, pos)

    def onMouseMove(self, x: int, y: int, xrelative: int, yrelative: int) -> None:
        pass

    def onMouseButtonClick(self, button: GameFramework.FRMouseButton, isReleased: bool) -> None:
        pass

    def onKeyPressed(self, key: FRKey) -> None:
        match key:
            case FRKey.RIGHT:
                self.head_pos.x += 1
            case FRKey.LEFT:
                self.head_pos.x -= 1
            case FRKey.DOWN:
                self.head_pos.y += 1
            case FRKey.UP:
                self.head_pos.y -= 1

    def onKeyReleased(self, k: FRKey) -> None:
        pass

    def Close(self) -> None:
        pass

    def GetTitle(self) -> str:
        return "Snake Game"


if __name__ == "__main__":
    game = MyGame()
    GameFramework.run(game)
