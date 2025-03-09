from vector import Vector
from Character.character import Character
import pygame
import os

DEFAULT = 0
WALKING_RIGHT = 1
WALKING_LEFT=3
ATTACKING = 2
JUMP = 4

class Archer(Character):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, arrows, xs, xy):
        self.sprites = {"default":[], "walk": [], "attack": [], "die": []}
        sprite_folder = 'images/archer'
        # Load images from subfolders (walk, attack, die)
        for action in self.sprites.keys():
            action_folder = os.path.join(sprite_folder, action)
            if os.path.exists(action_folder):
                for filename in sorted(os.listdir(action_folder)):
                    if filename.endswith(".png"):
                        image_path = os.path.join(action_folder, filename)
                        image = pygame.image.load(image_path)
                        self.sprites[action].append(image)
        self.current_action = "default"
        #self.current_sub_action = None  # Used for attack animations
        self.current_frame = 0
        self.image = self.sprites[self.current_action][self.current_frame]
        self.rect = self.image.get_rect()
        # self.expressions = []  # Instance attribute for sprite lists
        
        # aAttack = pygame.image.load("images/archer/aAttack.png")
        
        # walkingRight = []
        # walkingLeft = []

        # for i in range(1,8):
        #     image = pygame.image.load(f'images/archer/aWalk{i}.png')
        #     walkingRight.append(image)
        #     walkingLeft.append(pygame.transform.flip(image, True, False))

        # default = [walkingRight[0]]
        # attacking = [aAttack]
        
        # self.img = walkingRight[0] 
        # self.expressions.append(default)
        # self.expressions.append(walkingRight)
        # self.expressions.append(attacking)
        # self.expressions.append(walkingLeft)
        
        # # Set the initial expression state
        # self.expression = DEFAULT
        bounding_box = (x_pos, y_pos, self.image.get_width(), self.image.get_height())
        super().__init__(x_pos, y_pos, x_vel, y_vel, health, arrows, xs, xy, bounding_box)

    def sprint(self):
        self.velocity = self.velocity.times(2)
