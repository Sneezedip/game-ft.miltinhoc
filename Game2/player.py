import pygame
from enum import Enum
from over import Over


class PlayerDirection(Enum):
    LEFT = 0,
    RIGHT = 1


class Player(pygame.sprite.Sprite):
    def __init__(self, speed, width):
        super().__init__()
        self.screen_w = width
        self.image_r = pygame.image.load('player_r.png').convert_alpha()
        self.image = self.image_r
        self.rect = self.image.get_rect(midbottom=(width/2, 485))
        self.speed = speed
        self.direction = PlayerDirection.RIGHT
        self.hp = 100

    def toggle_image(self):
        if self.direction == PlayerDirection.RIGHT:
            self.direction = PlayerDirection.LEFT
            self.image = pygame.transform.flip(
                self.image, True, False)  # flips image to the left side
        else:
            self.direction = PlayerDirection.RIGHT
            self.image = self.image_r

    def damage(self, damage):
        if self.hp < damage:
            self.hp = 0
        else:
            self.hp -= damage

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.direction == PlayerDirection.RIGHT:
                self.toggle_image()
            if not self.outside_walls_collide():
                self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            if self.direction == PlayerDirection.LEFT:
                self.toggle_image()
            if not self.outside_walls_collide():
                self.rect.x += self.speed

    def outside_walls_collide(self):
        if self.rect.right >= self.screen_w and self.direction == PlayerDirection.RIGHT:
            return True
        if self.rect.left <= 0 and self.direction == PlayerDirection.LEFT:
            return True

    def update(self):
        self.player_input()
        self.dies()

    def dies(self):
        if self.hp == 0:
            self.kill()
            over = Over()
            over.Init()
