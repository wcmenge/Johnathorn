from vector import Vector
from Character.character import Character
import pygame

DEFAULT = 0
WALKING_RIGHT = 1
WALKING_LEFT=3
ATTACKING = 2
JUMP = 4

class Mage(Character):

    expressions = []
    expression = DEFAULT
    
    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys):

        ##Load Sprites
        mAttack = pygame.image.load("images/mage/mAttack.png")
        
        walkingRight = []
        walkingLeft = []
        for i in range(1,8):
            image = pygame.image.load(f'images/mage/mWalk{i}.png')
            walkingRight.append(image)
            walkingLeft.append(pygame.transform.flip(image, True, False))

        ##Setting Expressions from the sprite sheet
        attacking = []
        default = []
        attacking.append(mAttack)
        default.append(walkingRight[0])

        self.img = walkingRight[0] 
        self.expressions.append(default)
        self.expressions.append(walkingRight)
        self.expressions.append(attacking)
        self.expressions.append(walkingLeft)
        
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys, bounding_box)

    def heal(self, health, mana):
        if self.special < mana:
            print("NOT ENOUGH MANA")
        else:
            self.health += health
            self.special -= mana

    def attack(self, target):
        self.expression = ATTACKING
        super().attack(target)
        
