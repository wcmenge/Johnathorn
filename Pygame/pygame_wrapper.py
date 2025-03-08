from typing import List
import pygame
from pygame.event import Event
from pygame.joystick import JoystickType
from pygame.surface import Surface
from pygame.time import Clock

class PygameWrapper():
    window: Surface
    clock: Clock

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode()
        self.clock = pygame.time.Clock()

    @staticmethod
    def loadMusic(filepath: str) -> None:
        pygame.mixer.music.load(filepath)

    @staticmethod
    def playMusic() -> None:
        pygame.mixer.music.play()

    @staticmethod
    def setVolume(volume: float) -> None:
        pygame.mixer.music.set_volume(volume)

    @staticmethod
    def createSurfaceFromImage(filepath: str) -> Surface:
        return pygame.image.load(filepath)

    @staticmethod
    def transformSurfaceScale(surface: Surface, width: int, height: int) -> Surface:
        return pygame.transform.scale(surface, (width, height))

    @staticmethod
    def flipDisplay() -> None:
        pygame.display.flip()

    @staticmethod
    def getEvents() -> List[Event]:
        return pygame.event.get()

    @staticmethod
    def updateDisplay() -> None:
        pygame.display.update()

    @staticmethod
    def createJoystick() -> JoystickType:
        return pygame.joystick.Joystick(0)

    @staticmethod
    def getJoystickCount() -> int:
        return pygame.joystick.get_count()

    @staticmethod
    def quit() -> None:
        pygame.quit()

