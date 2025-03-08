from vector import Vector
from Enemy.enemy import Enemy
import pygame
import os

DEFAULT = 0
DEATH = 1

class Dragon(Enemy):
    steering = []

    def __init__(self, sheet, x_pos, y_pos, x_vel, y_vel, health, target):
        self.expressions = []
        self.load_images(sheet)
        self.expression = DEFAULT
        self.img = self.expressions[DEFAULT][0]  # Use the first image of the default expression
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        super().__init__(x_pos, y_pos, x_vel, y_vel, health, target, bounding_box)

    def load_images(self,sheet):
        self.expressions = {DEFAULT: [], DEATH: []}
        
        # Load default expression images
        self.expressions[DEFAULT].append(pygame.transform.scale2x(pygame.transform.flip(sheet.subsurface(0, 0, 115, 110), True, False)))

        # Load death expression images
        for i in range(1, 5):
            image = pygame.transform.scale2x(pygame.image.load(f'images/dragon/dragDeath{i}.png'))
            self.expressions[DEATH].append(image)

    # def attack(self):
    #     return

    def fireball(self):
        return

    def deepBreath(self):
        return
