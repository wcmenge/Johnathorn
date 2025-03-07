import pygame
from Character.character import Character
from Character.warrior import Warrior
from Enemy.dragon import Dragon
from Character.mage import Mage
from Character.druid import Druid
from Character.archer import Archer
from powerUp import PowerUp
import random

def play_game():
    char = start_screen()
    win = run_game(char)
    end_screen(win)
    
    

def start_screen():
    pygame.init()
    pygame.mixer.music.load("Sounds/opening_sound.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(.25)
    
    width = 3440#1280
    height = 1440#960
    my_win = pygame.display.set_mode((width, height))
    
    # Load background image once
    background = pygame.image.load("images/JOHNATHORN.png")
    new_background = pygame.transform.scale(background, (width, height))
    
    clock = pygame.time.Clock()
    keymap = {}
    
    while True:
        # Blit the background once per frame
        my_win.blit(new_background, (0, 0))
        pygame.display.flip()
        
        clock.tick(30)  # Limit frame rate to 30 FPS
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                keymap[event.key] = True
            elif event.type == pygame.KEYUP:
                keymap[event.key] = False

        # Check keys only once per frame after events are processed
        if keymap.get(pygame.K_w, False):
            return "Warrior"
        if keymap.get(pygame.K_m, False):
            return "Mage"
        if keymap.get(pygame.K_a, False):
            return "Archer"
        if keymap.get(pygame.K_d, False):
            return "Druid"

def end_screen(win):
    keepGoing = True
    width = 3440#1280
    height = 1440#960
    my_win = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    if win:
        background = pygame.image.load("images/END_SCREEN.png")
        new_background = pygame.transform.scale(background, (width, height))
        my_win.blit(new_background, (0, 0))
    else:
        background = pygame.image.load("images/END_SCREEN.png")
        new_background = pygame.transform.scale(background, (width, height))
        my_win.blit(new_background, (0, 0))
    while keepGoing:
        clock.tick(30)  # Limit frame rate to 30 FPS
        

        keymap = {}
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                key = event.key
                keymap[key] = True
            elif event.type == pygame.KEYUP:
                key = event.key
                keymap[key] = False
            if keymap.get(pygame.K_r, False):
                play_game()
                keepGoing = False
            if keymap.get(pygame.K_q, False):
                keepGoing = False

    pygame.quit()

def run_game(char):
    pygame.init()
    clock = pygame.time.Clock()
    width = 3440#1280
    height = 1440#960
    my_win = pygame.display.set_mode((width, height))
    keymap = {}

    dragon_sheet = pygame.image.load("images/thats_our_dragon.png")
    if char == "Warrior":
        char = Warrior(500, 500, 0, 0, 200, 100, 50, 50)
    elif char == "Mage":
        char = Mage(500, 500, 0, 0, 50, 100, 100, 100)
    elif char == "Druid":
        char = Druid(500, 500, 0, 0, 100, 100, 100, 100)
    else:
        char = Archer(500, 500, 0, 0, 100, 100, 300, 300)

    dragon = Dragon(dragon_sheet, 800, 500, 200, 200, 500, char)
    background = pygame.image.load("images/castle.jpg")
    new_background = pygame.transform.scale(background, (width, height))
    my_win.blit(new_background, (0, 0))

    sounds = ["Sounds/sound.ogg", "Sounds/sound1.ogg", "Sounds/sound2.ogg"]
    pygame.mixer.music.load(random.choice(sounds))
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    dt = 0
    keepGoing = True
    power = False
    while keepGoing:
        dt = clock.tick(60)
        #clock.tick(30)  # Limit frame rate to 30 FPS
        # if dt > 500:
        #     continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                key = event.key
                keymap[key] = True
            elif event.type == pygame.KEYUP:
                key = event.key
                keymap[key] = False
            elif event.type == pygame.JOYBUTTONDOWN:
                key = event.button
                keymap[key] = True
            elif event.type == pygame.JOYBUTTONUP:
                key = event.button
                keymap[key] = False

        chance = random.randint(0, 200)
        ptemp_img = pygame.image.load("images/p_up.png")
        p_img = pygame.transform.scale(ptemp_img, (25, 25))
        
        if chance == 25:
            p_up = PowerUp(p_img, random.randint(100, width), height - 25, "health")
            power = True
        elif chance == 50:
            p_up = PowerUp(p_img, random.randint(100, width), height - 25, "damage")
            power = True
        elif chance == 75:
            p_up = PowerUp(p_img, random.randint(100, width), height - 25, "speed")
            power = True

        my_win.blit(new_background, (0, 0))
        
        dragon.draw(my_win)
        dragon.draw_health(my_win)
        dragon.steering = []
        dragon.arrive(char, 1.0/10)
        dragon.apply_steering()
        dragon.move(dt, width, height)

        char.handle_input(keymap, dragon)        
        char.draw(my_win)
        char.draw_health(my_win)
        char.simulate(dt, width, height)

        if power:
            p_up.draw(my_win)
            power = p_up.collide(char)
            
        pygame.display.update()

        if char.health == 0:
            keepGoing = False
            return False
        if dragon.health == 0:
            return True

    pygame.quit()

play_game()
