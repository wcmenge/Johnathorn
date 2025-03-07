from vector import Vector
from Character.character import Character
import pygame

DEFAULT = 0
WALKING = 1
ATTACKING = 2

class Mage(Character):

    expressions = []
    expression = DEFAULT
    
    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys):
        mWalk1 = pygame.image.load("images/mage/mWalk1.png")
        self.img = mWalk1
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys, bounding_box)

        ##Load Sprites
        mAttack = pygame.image.load("images/mage/mAttack.png")
        mWalk1 = pygame.image.load("images/mage/mWalk1.png")
        mWalk2 = pygame.image.load("images/mage/mWalk2.png")
        mWalk3 = pygame.image.load("images/mage/mWalk3.png")
        mWalk4 = pygame.image.load("images/mage/mWalk4.png")
        mWalk5 = pygame.image.load("images/mage/mWalk5.png")
        mWalk6 = pygame.image.load("images/mage/mWalk6.png")
        mWalk7 = pygame.image.load("images/mage/mWalk7.png")
        
        ##Setting Expressions from the sprite sheet
        attacking = []
        default = []
        attacking.append(mAttack)
        default.append(mWalk1)

        # Create a list for walking right
        walking_right = [mWalk1, mWalk2, mWalk3, mWalk4, mWalk5, mWalk6, mWalk7]

        # Create a list for walking left by flipping each image horizontally
        walking_left = [pygame.transform.flip(img, True, False) for img in walking_right]

        self.expressions.append(default)
        self.expressions.append(walking_left)
        self.expressions.append(walking_right)
        self.expressions.append(attacking)
        
    def heal(self, health, mana):
        if self.special < mana:
            print("NOT ENOUGH MANA")
        else:
            self.health += health
            self.special -= mana

    def attack(self):
        self.expression = ATTACKING
        
