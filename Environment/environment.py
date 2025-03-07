import random
from typing import Any, List
import pygame
from pygame.surface import Surface

from Character.character import Character
from Enemy.enemy import Enemy

SKYBOX_CASTLE = "images/castle.jpg"
AMBIENT_SOUNDS_LIST = ["Sounds/sound.ogg", "Sounds/sound1.ogg", "Sounds/sound2.ogg"]

class Environment():
    skybox: Surface = pygame.image.load(SKYBOX_CASTLE)
    ambientSound: str = random.choice(AMBIENT_SOUNDS_LIST)

    baseGravity: float = 9.81
    platforms: List = []

    width: int
    height: int

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.skybox = pygame.transform.scale(self.skybox,(width, height))

    def playAmbientSound(self):
        pygame.mixer.music.load(self.ambientSound)
        pygame.mixer.music.play()

    def stopAmbientSound(self):
        pygame.mixer.music.stop()

    def pickRandomSoundFromList(self):
        self.ambientSound = random.choice(AMBIENT_SOUNDS_LIST)

    def initializeEnvironment(self) -> None:
        pass

    def applyGravity(self, target: Enemy | Character) -> None:
        pass

    pass

class Window():
    window: Surface
    width: int
    height: int

    environment: Environment

    def __init__(self, width, height, window) -> None:
        self.width = width
        self.height = height
        self.window = window 


