from vector import Vector
from Character.character import Character
import pygame

DEFAULT = 0
WALKING = 1
ATTACKING = 2

class Druid (Character):

        expressions = []
        expression = DEFAULT

        def __init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys):
                dWalk1 = pygame.image.load("images/druid/dWalk1.png")
                self.img = dWalk1
                bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
                Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys, bounding_box)
                self.form = "normal"

        ##Load Sprites
                dAttack1 = pygame.image.load("images/druid/dAttack1.png")
                dAttack2 = pygame.image.load("images/druid/dAttack2.png")
                dWalk2 = pygame.image.load("images/druid/dWalk2.png")
                dWalk3 = pygame.image.load("images/druid/dWalk3.png")
                dWalk4 = pygame.image.load("images/druid/dWalk4.png")
                dWalk5 = pygame.image.load("images/druid/dWalk5.png")
                dWalk6 = pygame.image.load("images/druid/dWalk6.png")
                dWalk7 = pygame.image.load("images/druid/dWalk7.png")

                walking = [] 
                attacking = []
                default = []
                default.append(dWalk1)
                walking.append(dWalk1)
                walking.append(dWalk2)
                walking.append(dWalk3)
                walking.append(dWalk4)
                walking.append(dWalk5)
                walking.append(dWalk6)
                walking.append(dWalk7)
                attacking.append(dAttack1)
                attacking.append(dAttack2)

                self.expressions.append(default)
                self.expressions.append(walking)
                self.expressions.append(attacking)

        def attack(self):
            self.expression = ATTACKING

        def shape_shift(self, form, mana):
                if self.special < mana:
                    print("NOT ENOUGH MANA")
                else:
                    self.form = form
