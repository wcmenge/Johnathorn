from vector import Vector
from Character.character import Character
import pygame

DEFAULT = 0
WALKING_RIGHT = 1
WALKING_LEFT=3
ATTACKING = 2
JUMP = 4


class Warrior(Character):

    expressions = []
    expression = DEFAULT


    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, armour, xs, ys):
        attacking = []
        ##Load sprites

        for i in range(1,5):
            image = pygame.image.load(f'images/warrior/wAttack{i}.png')
            attacking.append(image)


        walkingRight = []
        walkingLeft = []
        for i in range(1,8):
            image = pygame.image.load(f'images/warrior/wWalk{i}.png')
            walkingRight.append(image)
            walkingLeft.append(pygame.transform.flip(image, True, False))

        default = []
        default.append(walkingRight[0])

        self.armour = armour
        self.img = walkingLeft[0]
        self.expressions.append(default)
        self.expressions.append(walkingRight)
        self.expressions.append(attacking)
        self.expressions.append(walkingLeft)

        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, armour, xs, ys, bounding_box)

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
