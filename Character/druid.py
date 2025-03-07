from vector import Vector
from Character.character import Character
import pygame

DEFAULT = 0
WALKING_RIGHT = 1
WALKING_LEFT=3
ATTACKING = 2
JUMP = 4

class Druid (Character):

        expressions = []
        expression = DEFAULT

        def __init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys):

                ##Load Sprites
                dAttack1 = pygame.image.load("images/druid/dAttack1.png")
                dAttack2 = pygame.image.load("images/druid/dAttack2.png")

                walkingRight = []
                walkingLeft = []
                for i in range(1,7):
                    image = pygame.image.load(f'images/druid/dWalk{i}.png')
                    walkingRight.append(image)
                    walkingLeft.append(pygame.transform.flip(image, True, False))


                attacking = []
                default = []
                default.append(walkingRight[0])
                attacking.append(dAttack1)
         
                # Create a list for walking left by flipping each image horizontally
                attacking.append(dAttack2)

                self.form = "normal"
                self.img = walkingRight[0] 
                self.expressions.append(default)
                self.expressions.append(walkingRight)
                self.expressions.append(attacking)
                self.expressions.append(walkingLeft)
                bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
                Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys, bounding_box)

        def attack(self, target):
            self.expression = ATTACKING
            super().attack(target)

        def shape_shift(self, form, mana):
                if self.special < mana:
                    print("NOT ENOUGH MANA")
                else:
                    self.form = form
