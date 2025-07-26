import math
from enum import Enum, auto
from abc import ABC, abstractmethod
import pygame
import time


class Sprite:
    def __init__(self, path: str):
        self.surface = pygame.image.load(path)
        self.size = pygame.math.Vector2(self.surface.get_size())

    def draw(self, pos: pygame.math.Vector2, rotation: float = 0.0) -> None:
        rotated_surface = pygame.transform.rotate(self.surface, -rotation * 180 / math.pi)
        rect = rotated_surface.get_rect(center=pos + self.size * 0.5)
        pygame.display.get_surface().blit(rotated_surface, rect)

    def get_size(self) -> pygame.math.Vector2:
        return self.size

    def set_size(self, size: pygame.math.Vector2) -> None:
        self.surface = pygame.transform.scale(self.surface, size)
        self.size = size

    def destroy(self) -> None:
        del self

class FRKey(Enum):
    RIGHT = auto()
    LEFT = auto()
    DOWN = auto()
    UP = auto()
    COUNT = auto()

class FRMouseButton(Enum):
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()
    COUNT = auto()



def drawTestBackground() -> None:
    surface = pygame.display.get_surface()
    surface.fill((128, 128, 128))


def getScreenSize() -> tuple[int, int]:
    surface = pygame.display.get_surface()
    return surface.get_width(), surface.get_height()


def getTickCount() -> int:
    return int(time.time() * 1000)


def showCursor(show: bool) -> None:
    pygame.mouse.set_visible(show)


class Framework(ABC):
    @abstractmethod
    def PreInit(self) -> tuple[int, int, bool]:
        """Return width, height and fullscreen values"""
        pass

    @abstractmethod
    def Init(self) -> bool:
        """Return True if initialization successful, False otherwise"""
        pass

    @abstractmethod
    def Close(self) -> None:
        pass

    @abstractmethod
    def Tick(self) -> bool:
        """Return True to exit the application"""
        pass

    @abstractmethod
    def onMouseMove(self, x: int, y: int, xrelative: int, yrelative: int) -> None:
        pass

    @abstractmethod
    def onMouseButtonClick(self, button: FRMouseButton, isReleased: bool) -> None:
        pass

    @abstractmethod
    def onKeyPressed(self, k: FRKey) -> None:
        pass

    @abstractmethod
    def onKeyReleased(self, k: FRKey) -> None:
        pass

    @abstractmethod
    def GetTitle(self) -> str:
        pass


def run(framework: Framework) -> int:
    pygame.init()
    width, height, fullscreen = framework.PreInit()
    flags = pygame.FULLSCREEN if fullscreen else 0
    pygame.display.set_mode((width, height), flags)
    pygame.display.set_caption(framework.GetTitle())

    if not framework.Init():
        return 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                framework.onMouseMove(event.pos[0], event.pos[1], event.rel[0], event.rel[1])
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                button = None
                if event.button == 1:
                    button = FRMouseButton.LEFT
                elif event.button == 2:
                    button = FRMouseButton.MIDDLE
                elif event.button == 3:
                    button = FRMouseButton.RIGHT
                if button:
                    framework.onMouseButtonClick(button, event.type == pygame.MOUSEBUTTONUP)
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key = None
                if event.key == pygame.K_RIGHT:
                    key = FRKey.RIGHT
                elif event.key == pygame.K_LEFT:
                    key = FRKey.LEFT
                elif event.key == pygame.K_DOWN:
                    key = FRKey.DOWN
                elif event.key == pygame.K_UP:
                    key = FRKey.UP

                if key:
                    if event.type == pygame.KEYDOWN:
                        framework.onKeyPressed(key)
                    else:
                        framework.onKeyReleased(key)

        if framework.Tick():
            running = False

        pygame.display.flip()

    framework.Close()
    pygame.quit()
    return 0
