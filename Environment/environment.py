from typing import List
import pygame
from pygame.surface import Surface

from Character.character import Character
from Enemy.enemy import Enemy

class Environment():
    skybox: Surface
    baseGravity: float = 9.81
    platforms: List = []

    def initializeEnvironment(self) -> None:
        pass

    def applyGravity(self, target: Enemy | Character) -> None:
        pass

    pass

