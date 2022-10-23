import pygame
import random
from enum import Enum


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, type):
        super().__init__()
        self.image = pygame.image.load(type).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(
            random.randint(0, width - self.image.get_width()), 0))
        self.speed = random.randint(1, 20)
        self.damage = 20

    def update(self):
        self.rect.y += self.speed
        self.destroy()

    def remove(self):
        self.kill()

    def destroy(self):
        if self.rect.y >= 450:
            self.kill()


class ObstacleType(Enum):
    METEORITE = 'meteor.png'
    SQUARE = 'obstacle.png'
    SPEED = 'speed.png'


class ObstacleFactory():
    def __init__(self, width):
        super().__init__()
        self.width = width

    def get_obstacle(self):
        type = random.choice(list(ObstacleType))
        print(type)
        return Obstacle(self.width, type.value)
