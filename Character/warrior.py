from vector import Vector
from Character.character import Character
import pygame
DEFAULT = 0
WALKING = 1
ATTACKING = 2

class Warrior(Character):

    expressions = []
    expression = DEFAULT


    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, armour, xs, ys):
        wWalk1 = pygame.image.load("images/warrior/wWalk1.png")
        self.img = wWalk1
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, armour, xs, ys, bounding_box)
        self.armour = armour
        walking = []
        attacking = []
        ##Load sprites
        wAttack1 = pygame.image.load("images/warrior/wAttack1.png")
        wAttack2 = pygame.image.load("images/warrior/wAttack2.png")
        wAttack3 = pygame.image.load("images/warrior/wAttack3.png")
        wAttack4 = pygame.image.load("images/warrior/wAttack4.png")
        wAttack5 = pygame.image.load("images/warrior/wAttack5.png")
        wWalk2 = pygame.image.load("images/warrior/wWalk2.png")
        wWalk3 = pygame.image.load("images/warrior/wWalk3.png")
        wWalk4 = pygame.image.load("images/warrior/wWalk4.png")
        wWalk5 = pygame.image.load("images/warrior/wWalk5.png")
        wWalk6 = pygame.image.load("images/warrior/wWalk6.png")
        wWalk7 = pygame.image.load("images/warrior/wWalk7.png")
        wWalk8 = pygame.image.load("images/warrior/wWalk8.png")
        walking.append(wWalk1)
        walking.append(wWalk2)
        walking.append(wWalk3)
        walking.append(wWalk4)
        walking.append(wWalk5)
        walking.append(wWalk6)
        walking.append(wWalk7)
        walking.append(wWalk8)
        attacking.append(wAttack1)
        attacking.append(wAttack2)
        attacking.append(wAttack3)
        attacking.append(wAttack4)
        attacking.append(wAttack5)
        default = []
        default.append(wWalk1)
        self.expressions.append(default)
        self.expressions.append(walking)
        self.expressions.append(attacking)

        
##        ##Setting Expressions from the sprite sheet
##        self.expressions["default"] = sheet.subsurface(0,0,115,105)
##        self.expressions["walkLeft"] = pygame.transform.flip(sheet.subsurface(115,230,105,210), True, False)
##        self.expressions["walkRight"] = sheet.subsurface(115,230,105,210)
##        #self.expressions["attack"] = sheet.subsurface(815,210,930,315)
##        #self.expressions["dead"] = sheet.subsurface(815,315,930,420)
##        

    def attack(self, target):
        self.expression = ATTACKING
        if self.collide(target):
            target.remove_health(self.damage)

        

    def block(self):
        return

    def set_armour(self, new_armour):
        self.armour += new_armour

    def get_armour(self):
        return self.armour
