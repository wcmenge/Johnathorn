from vector import Vector
from enemy import Enemy
import pygame



class Dragon(Enemy):
    expressions = {}
    expression = "default"

    def __init__(self, sheet, x_pos, y_pos, x_vel, y_vel, health, target):
        self.expressions["default"] = pygame.transform.scale2x(pygame.transform.flip(sheet.subsurface(0,0,115,110), True, False))
        self.img = self.expressions["default"]
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        Enemy.__init__(self, sheet, x_pos, y_pos, x_vel, y_vel, health, target, bounding_box)

        ##Setting Expressions


        # def attack(self):
        #     return

        def fireball(self):
            return

        def deepBreath(self):
            return
