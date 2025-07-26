import pygame
from pygame import Vector2

from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.Simulation.Field import Field
from src.Simulation.Snake import Snake
from src.ThirdParty import GameFramework
from src.ThirdParty.GameFramework import Framework, Sprite, FRKey

class MyGame(Framework):
    def __init__(self):
        self.font = None
        self.window_size = Vector2(640, 640)
        self.field = Field(self.window_size, 11)
        self.snake = Snake(Vector2(self.field.cells//2, self.field.cells//2))

    def PreInit(self) -> tuple[int, int, bool]:
        pygame.font.init()
        return int(self.window_size.x), int(self.window_size.y), False

    def Init(self) -> bool:
        SPRITE_FACTORY.init('images', self.field.cell_size)
        self.font = pygame.font.SysFont('Arial', 10)
        self.snake.init(self.field.cell_size)
        return True

    def Tick(self) -> bool:
        self.draw_test_field()
        self.snake.draw(self.field.cell_size)
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
