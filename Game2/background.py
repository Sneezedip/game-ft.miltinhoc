import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_location):
        super().__init__()
        self.image = pygame.image.load(image_location)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0,0]
