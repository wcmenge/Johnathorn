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
        # Load the initial sprite and determine the bounding box
        aWalk1 = pygame.image.load("images/archer/aWalk1.png")
        self.img = aWalk1
        bounding_box = (x_pos, y_pos, self.img.get_width(), self.img.get_height())
        super().__init__(x_pos, y_pos, x_vel, y_vel, health, arrows, xs, xy, bounding_box)
        
        # Set up sprite expressions for different states
        self.expressions = []  # Instance attribute for sprite lists
        
        # Load sprites for various animations
        #walking = []
        aAttack = pygame.image.load("images/archer/aAttack.png")
        aJump = pygame.image.load("images/archer/aJump.png")  # aJump is loaded but not used in this example

        aWalk2 = pygame.image.load("images/archer/aWalk2.png")
        aWalk3 = pygame.image.load("images/archer/aWalk3.png")
        aWalk4 = pygame.image.load("images/archer/aWalk4.png")
        aWalk5 = pygame.image.load("images/archer/aWalk5.png")
        aWalk6 = pygame.image.load("images/archer/aWalk6.png")
        aWalk7 = pygame.image.load("images/archer/aWalk7.png")
        aWalk8 = pygame.image.load("images/archer/aWalk8.png")
        
        # Create a list for walking right
        walking_right = [aWalk1, aWalk2, aWalk3, aWalk4, aWalk5, aWalk6, aWalk7, aWalk8]

        # Create a list for walking left by flipping each image horizontally
        walking_left = [pygame.transform.flip(img, True, False) for img in walking_right]
        # walking.append(aWalk1)
        # walking.append(aWalk2)
        # walking.append(aWalk3)
        # walking.append(aWalk4)
        # walking.append(aWalk5)
        # walking.append(aWalk6)
        # walking.append(aWalk7)
        # walking.append(aWalk8)

        default = [aWalk1]
        attacking = [aAttack]
        
        self.expressions.append(default)
        self.expressions.append(walking_right)
        self.expressions.append(attacking)
        self.expressions.append(walking_left)
        
        # Set the initial expression state
        self.expression = DEFAULT

    def sprint(self):
        self.velocity = self.velocity.times(2)
