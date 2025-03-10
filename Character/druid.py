from vector import Vector
from Character.character import Character
import pygame
import os

DEFAULT = 0
WALKING_RIGHT = 1
WALKING_LEFT=3
ATTACKING = 2
JUMP = 4

class Druid (Character):

        expressions = []
        expression = DEFAULT

        def __init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys):
            self.sprites = {"default":[], "walk": [], "attack": [], "die": []}
            sprite_folder = 'images/druid'
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
            ##Load Sprites
            # dAttack1 = pygame.image.load("images/druid/dAttack1.png")
            # dAttack2 = pygame.image.load("images/druid/dAttack2.png")

            # walkingRight = []
            # walkingLeft = []
            # for i in range(1,7):
            #     image = pygame.image.load(f'images/druid/dWalk{i}.png')
            #     walkingRight.append(image)
            #     walkingLeft.append(pygame.transform.flip(image, True, False))


            # attacking = []
            # default = []
            # default.append(walkingRight[0])
            # attacking.append(dAttack1)
         
            # # Create a list for walking left by flipping each image horizontally
            # attacking.append(dAttack2)

            # self.form = "normal"
            # self.img = walkingRight[0] 
            # self.expressions.append(default)
            # self.expressions.append(walkingRight) 
            # self.expressions.append(attacking)
            # self.expressions.append(walkingLeft)
            bounding_box = (x_pos, y_pos, self.image.get_width(), self.image.get_height())
            Character.__init__(self, x_pos, y_pos, x_vel, y_vel, health, mana, xs, ys, bounding_box)

        def attack(self, target):
            self.expression = ATTACKING
            super().attack(target)

        def shape_shift(self, form, mana):
                if self.special < mana:
                    print("NOT ENOUGH MANA")
                else:
                    self.form = form
