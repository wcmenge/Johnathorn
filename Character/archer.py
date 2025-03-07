from vector import Vector
from Character.character import Character
import pygame

DEFAULT = 0
WALKING_RIGHT = 1
WALKING_LEFT=3
ATTACKING = 2
JUMP = 4

class Archer(Character):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, arrows, xs, xy):
        self.expressions = []  # Instance attribute for sprite lists
        
        aAttack = pygame.image.load("images/archer/aAttack.png")
        
        walkingRight = []
        walkingLeft = []

        for i in range(1,8):
            image = pygame.image.load(f'images/archer/aWalk{i}.png')
            walkingRight.append(image)
            walkingLeft.append(pygame.transform.flip(image, True, False))

        default = [walkingRight[0]]
        attacking = [aAttack]
        
        self.img = walkingRight[0] 
        self.expressions.append(default)
        self.expressions.append(walkingRight)
        self.expressions.append(attacking)
        self.expressions.append(walkingLeft)
        
        # Set the initial expression state
        self.expression = DEFAULT
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        super().__init__(x_pos, y_pos, x_vel, y_vel, health, arrows, xs, xy, bounding_box)

    def sprint(self):
        self.velocity = self.velocity.times(2)
