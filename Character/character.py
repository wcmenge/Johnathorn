from vector import Vector
import pygame

DEFAULT = 0
WALKING_RIGHT = 1
ATTACKING = 2
WALKING_LEFT = 3

class Character:

    animspeed = 20.0  # frames per second
    animtimer = 0.0
    animidx = 0

    def __init__(self, x_pos, y_pos, x_vel, y_vel, health, special, xs, ys, bounding_box):
        self.health = health
        self.special = special
        self.pos = Vector(0.0, 0.0)
        self.pos.x = x_pos
        self.pos.y = y_pos
        self.velocity = Vector(0.0, 0.0)
        self.velocity.x = x_vel
        self.velocity.y = y_vel
        self.buff = None
        self.debuff = None
        self.xs = xs
        self.ys = ys
        self.damage = 25
        self.bbox = bounding_box
        self.expression = DEFAULT  # initialize expression
        # self.expressions should be set up elsewhere with appropriate image lists

    def set_vel(self, new_x, new_y):
        self.velocity = (new_x, new_y)

    def get_vel(self):
        return self.velocity

    def add_health(self, health):
        self.health += health

    def remove_health(self, health):
        self.health -= health

    def add_buff(self, buff):
        if buff == "health":
            self.add_health(25)
        elif buff == "damage":
            self.damage *= 2
        else:
            self.velocity = self.velocity.times(1.5)

    def add_debuff(self, debuff):
        self.debuff = debuff

    def get_buff(self):
        return self.buff

    def get_debuff(self):
        return self.debuff

    def set_pos(self, new_x, new_y):
        self.pos = (new_x, new_y)

    def get_pos(self):
        return self.pos

    def attack(self, target):
        self.expression = ATTACKING
        self.animidx = 0  # Reset animation index when switching to the attack state
        target.remove_health(1)

    def draw(self, window):
        imgs = self.expressions[self.expression]

        if self.animtimer > 1000.0 / self.animspeed:
            self.animidx = (self.animidx + 1) % len(imgs)
            self.animtimer = 0

        img = imgs[self.animidx]
        window.blit(img, (round(self.pos.x), round(self.pos.y)))

    def jump(self):
        start_jump = self.pos.y
        while self.pos.y > start_jump - 30:
            self.pos.y -= 10

    def move(self, millisecs):
        self.pos.y += self.velocity.y * float(millisecs) / 1000
        self.pos.x += self.velocity.x * float(millisecs) / 1000
        if self.velocity.x == 0:
            self.animtimer = 0
            self.animidx = 0

    def simulate(self, millisecs, width, height):
        self.animtimer += millisecs
        self.move(millisecs)
        self.bounce(width, height)
        self.simulateGravity()

    def bounce(self, width, height):
        imgs = self.expressions[self.expression]
        if (self.pos.x + imgs[0].get_width()) > width:
            self.pos.x = width - imgs[0].get_width()
        elif self.pos.x < 0:
            self.pos.x = 0

        if (self.pos.y + imgs[0].get_height()) > height:
            self.pos.y = height - imgs[0].get_height()
        elif self.pos.y < 0:
            self.pos.y = 0
            self.velocity.y = -self.velocity.y

    def simulateGravity(self):
        if self.pos.y + 105 < 960:
            self.velocity.y += 10

    # def handle_input(self, keymap, target):
    def handle_input(self, keymap, target, joystick=None):
        self.velocity.x = 0  # Reset velocity before applying movement

        # Keyboard Controls
        if keymap.get(pygame.K_w, False):
            self.jump()
        if keymap.get(pygame.K_a, False):
            self.velocity.x -= self.xs
            self.expression = WALKING_LEFT
        if keymap.get(pygame.K_d, False):
            self.velocity.x += self.xs
            self.expression = WALKING_RIGHT
        if keymap.get(pygame.K_s, False):
            self.attack(target)
            self.expression = ATTACKING

        # Controller Support
        if joystick:
            axis_x = joystick.get_axis(0)  # Left stick horizontal movement
            a_button = joystick.get_button(0)  # A button for jumping
            x_button = joystick.get_button(2)  # X button for attacking

            # Movement using the left stick
            if abs(axis_x) > 0.2:  # Deadzone to avoid drift
                self.velocity.x = axis_x * self.xs
                self.expression = WALKING_LEFT if axis_x < 0 else WALKING_RIGHT

            # Jumping with the A button
            if a_button:
                self.jump()

            # Attacking with the X button
            if x_button:
                self.attack(target)
                self.expression = ATTACKING

    def draw_health(self, window):
        left = int(window.get_width() * 0.03)
        top = int(window.get_width() * 0.05)
        height = int(window.get_height() * 0.02)
        width = self.health * 100 / (window.get_width() / 10)
        area = window.subsurface((left, top, width, height))
        area.fill(pygame.Color("green"))
        area.blit(window, (left, top))

    def get_bbox(self):
        """
        Calculates the screen coordinate of the bounding box.
        """
        return pygame.Rect(self.pos.x, self.pos.y, self.bbox[2], self.bbox[3])

    def collide(self, other):
        """
        Uses pygame's built in collision detection to check whether
        two sprites collide based on their bounding boxes.
        """
        return self.get_bbox().colliderect(other.get_bbox())
