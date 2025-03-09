from vector import Vector
from Enemy.enemy import Enemy
import pygame
import os
class Minotaur(Enemy):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, target):
        super().__init__()
        self.sprites = {"default":[], "walk": [], "attack": {}, "die": []}
        sprite_folder = 'images/minotaur'
        # Load images from subfolders (walk, attack, die)
        for action in ["default","walk", "die"]:
            action_folder = os.path.join(sprite_folder, action)
            if os.path.exists(action_folder):
                for filename in sorted(os.listdir(action_folder)):
                    if filename.endswith(".png"):
                        image_path = os.path.join(action_folder, filename)
                        image = pygame.image.load(image_path)
                        self.sprites[action].append(image)
        
        # Handle attack subcategories (e.g., shoot, melee)
        attack_folder = os.path.join(sprite_folder, "attack")
        if os.path.exists(attack_folder):
            for sub_action in os.listdir(attack_folder):
                sub_action_path = os.path.join(attack_folder, sub_action)
                if os.path.isdir(sub_action_path):
                    self.sprites["attack"][sub_action] = []
                    for filename in sorted(os.listdir(sub_action_path)):
                        if filename.endswith(".png"):
                            image_path = os.path.join(sub_action_path, filename)
                            image = pygame.image.load(image_path)
                            self.sprites["attack"][sub_action].append(image)
        
        self.current_action = "default"
        self.current_sub_action = None  # Used for attack animations
        self.current_frame = 0
        self.image = self.sprites[self.current_action][self.current_frame]
        self.rect = self.image.get_rect()
    
    def attack(self):
        if "melee" in self.sprites["attack"]:
            self.set_action("attack", "melee")
        else:
            print("Melee attack animation not found.")
        return super().attack()