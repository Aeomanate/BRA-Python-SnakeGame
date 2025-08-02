import pygame
from pygame import Vector2

from src.DrawDelegates.SpriteFactory import SPRITE_FACTORY
from src.Simulation.Field import Field
from src.Simulation.Snake import Snake
from src.ThirdParty import GameFramework
from src.ThirdParty.GameFramework import Framework, FRKey

from src.Simulation.Simulation import Simulation
from src.DrawDelegates.DrawerPygame import DrawerPygame


class MyGame(Framework):
    def __init__(self):
        self.font = None
        self.window_size = Vector2(640, 640)
        self.FIELD_SIZE = 11
        self.simulation = None
        self.game_over = False
        self.score = 0
        self.drawer = None

    def PreInit(self) -> tuple[int, int, bool]:
        pygame.font.init()
        return int(self.window_size.x), int(self.window_size.y), False

    def Init(self) -> bool:
        self.simulation = Simulation(self.FIELD_SIZE, self.window_size)
        self.drawer = DrawerPygame(self.simulation.field.cell_size)
        SPRITE_FACTORY.init('images', self.simulation.field.cell_siz)
        return True

    def Tick(self) -> bool:
        if self.game_over:
            self.show_game_over()
            return False

        if not self.simulation.update(pygame.time.get_ticks()):
            self.game_over = True
            return False

        self.simulation.draw(self.drawer, self.font)
        self.score = len(self.simulation.snake.body) - 1
        return False

    def onMouseMove(self, x: int, y: int, xrelative: int, yrelative: int) -> None:
        pass

    def onMouseButtonClick(self, button: GameFramework.FRMouseButton, isReleased: bool) -> None:
        pass

    def onKeyPressed(self, key: FRKey) -> None:
        if self.game_over and (key == FRKey.SPACE or key in [FRKey.UP, FRKey.DOWN, FRKey.LEFT, FRKey.RIGHT]):
            self.restart_game()
            return

        direction = None
        if key == FRKey.RIGHT:
            direction = Vector2(1, 0)
        elif key == FRKey.LEFT:
            direction = Vector2(-1, 0)
        elif key == FRKey.DOWN:
            direction = Vector2(0, 1)
        elif key == FRKey.UP:
            direction = Vector2(0, -1)
        if direction:
            self.simulation.set_direction(direction)

    def show_game_over(self):
        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))
        msg1 = f"Game Over! Ваш счёт: {self.score}"
        msg2 = "Нажмите пробел или Enter для перезапуска"
        font_big = pygame.font.SysFont('Arial', 32)
        font_small = pygame.font.SysFont('Arial', 20)
        text1 = font_big.render(msg1, True, (255, 0, 0))
        text2 = font_small.render(msg2, True, (255, 255, 255))
        surface.blit(text1, (self.window_size.x // 2 - text1.get_width() // 2, self.window_size.y // 2 - 40))
        surface.blit(text2, (self.window_size.x // 2 - text2.get_width() // 2, self.window_size.y // 2 + 10))
        pygame.display.flip()

    def restart_game(self):
        self.simulation = Simulation(self.FIELD_SIZE, self.window_size)
        self.game_over = False
        self.score = 0

    def onKeyReleased(self, k: FRKey) -> None:
        pass

    def Close(self) -> None:
        pass

    def GetTitle(self) -> str:
        return "Snake Game"


if __name__ == "__main__":
    game = MyGame()
    GameFramework.run(game)
