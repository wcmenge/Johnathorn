import pygame
import sys
from Enemy.dragon import Dragon
from Environment.environment import Environment, Window
from Character.character_defaults import CharacterDefault
from powerUp import PowerUp
import random
import pygame_menu
import os

R2BUTTON = 5
L2BUTTON = 4
SQUAREBUTTON = 2
XBUTTON = 0

WIDTH = 1920
HEIGHT = 1080
FULLSCREEN = False

def set_resolution(value, resolution):
    global WIDTH, HEIGHT, FULLSCREEN
    if resolution == 'Full Screen':
        FULLSCREEN = True
        info = pygame.display.Info()
        WIDTH, HEIGHT = info.current_w, info.current_h
    else:
        FULLSCREEN = False
        WIDTH, HEIGHT = resolution

def play_game():
        #startMenu()
        char = character_selection_screen()
        win = run_game(char)
        end_screen(win)

def startMenu():
    pygame.init()
    my_win = pygame.display.set_mode((WIDTH, HEIGHT))
    width = WIDTH
    height = HEIGHT
    exit = False
    menu = pygame_menu.Menu('Select Resolution', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_DARK)

    resolutions = [
        ('1920x1080 (1080p)', (1920, 1080)),
        ('2560x1440 (1440p)', (2560, 1440)),
        ('3840x2160 (4K)', (3840, 2160)),
        ('2560x1080 (UWHD)', (2560, 1080)),
        ('3440x1440 (UWQHD)', (3440, 1440)),
        ('5120x2160 (5K2K)', (5120, 2160)),
        ('Full Screen', 'Full Screen')
    ]

    menu.add.selector('Resolution :', resolutions, onchange=set_resolution)
    menu.add.button('Start Game', play_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    resolution_selected = False

    while not exit:
        my_win.blit(pygame.Surface((WIDTH, HEIGHT)), (0, 0))
        events = pygame.event.get()
        for event in events:
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if menu.is_enabled():
            menu.update(events)
            menu.draw(my_win)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

        if not menu.is_enabled():
            resolution_selected = True
            break

    # Update display mode after resolution is selected
    flags = pygame.FULLSCREEN if FULLSCREEN else 0
    pygame.display.set_mode((WIDTH, HEIGHT), flags)

    return resolution_selected

def start_screen():
    pygame.mixer.music.load("Sounds/opening_sound.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(.1)

    flags = pygame.FULLSCREEN if FULLSCREEN else 0
    my_win = pygame.display.set_mode((WIDTH, HEIGHT), flags)

    if not FULLSCREEN:
        # Center the window on the screen
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(pygame.display.Info().current_w - WIDTH) // 2},{(pygame.display.Info().current_h - HEIGHT) // 2}"

    # Load background image once
    background = pygame.image.load("images/JOHNATHORN.png")
    new_background = pygame.transform.scale(background, (my_win.get_width(), my_win.get_height()))

    clock = pygame.time.Clock()
    keymap = {}

    while True:
        # Blit the background once per frame
        my_win.blit(new_background, (0, 0))
        pygame.display.flip()

        clock.tick(30)  # Limit frame rate to 30 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

def character_selection_screen():
    width = WIDTH
    height = HEIGHT
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
                pygame.quit()
                sys.exit()
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

    flags = pygame.FULLSCREEN if FULLSCREEN else 0
    my_win = pygame.display.set_mode((WIDTH, HEIGHT), flags)

    if not FULLSCREEN:
        # Center the window on the screen
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(pygame.display.Info().current_w - WIDTH) // 2},{(pygame.display.Info().current_h - HEIGHT) // 2}"

    clock = pygame.time.Clock()
    background = pygame.image.load("images/END_SCREEN.png")
    new_background = pygame.transform.scale(background, (WIDTH, HEIGHT))
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
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keymap.get(pygame.K_r, False):
                play_game()
                keepGoing = False
            if keymap.get(pygame.K_q, False):
                keepGoing = False

    pygame.quit()

def initalizePygame(char):
    pygame.init()

    flags = pygame.FULLSCREEN if FULLSCREEN else 0
    myWindow: Window = Window(WIDTH, HEIGHT, pygame.display.set_mode((WIDTH, HEIGHT), flags))
    environment: Environment = Environment(WIDTH, HEIGHT)

    if not FULLSCREEN:
        # Center the window on the screen
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(pygame.display.Info().current_w - WIDTH) // 2},{(pygame.display.Info().current_h - HEIGHT) // 2}"

    clock = pygame.time.Clock()
    keymap = {}

    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    char = CharacterDefault.handleSelection(char)

    myWindow.window.blit(environment.skybox, (0, 0))
    environment.playAmbientSound()

    return myWindow, clock, keymap, joystick, char, environment

def run_game(char):
    my_win, clock, keymap, joystick, char, environment = initalizePygame(char)

    dragon_sheet = pygame.image.load("images/thats_our_dragon.png")
    dragon = Dragon(dragon_sheet, 800, 500, 200, 200, 500, char)

    dt = 0
    keepGoing = True
    power = False
    p_up = None
    while keepGoing:
        dt = clock.tick(60)
        #clock.tick(30)  # Limit frame rate to 30 FPS
        # if dt > 500:
        #     continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
                sys.exit()
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

        if not power and p_up == None:
            if chance == 25:
                p_up = PowerUp(p_img, random.randint(100, WIDTH), HEIGHT - 25, "health")
                power = True
            elif chance == 50:
                p_up = PowerUp(p_img, random.randint(100, WIDTH), HEIGHT - 25, "damage")
                power = True
            elif chance == 75:
                p_up = PowerUp(p_img, random.randint(100, WIDTH), HEIGHT - 25, "speed")
                power = True

        my_win.window.blit(environment.skybox, (0, 0))

        dragon.draw(my_win.window)
        dragon.draw_health(my_win.window)

        dragon.arrive(char, 1.0/10)
        dragon.apply_steering()
        dragon.move(dt, WIDTH, HEIGHT)

        char.handle_input(keymap, dragon, joystick)

        char.draw(my_win.window)
        char.draw_health(my_win.window)
        char.simulate(dt, WIDTH, HEIGHT)

        if power and p_up != None:
            p_up.draw(my_win.window)
            power = p_up.collide(char)
            if not power:
                p_up = None

        pygame.display.update()

        if char.health == 0:
            keepGoing = False
            return False
        if not dragon.isAlive():
            # start a timer
            dragon.die()
            return True

    pygame.quit()

startMenu()
