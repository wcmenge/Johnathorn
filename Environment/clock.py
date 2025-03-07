
import pygame
from pygame.time import Clock


class GameClock():
    gameClock: Clock = pygame.time.Clock()
    
    def __init__(self) -> None:
        pass

    def tickClock(self, tick: int) -> None:
        self.gameClock.tick(tick)

    pass

