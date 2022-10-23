from background import Background
import pygame


class Menu():
    def __init__(self):
        self.menu = True
        self.background = Background('background2.png')
        self.font = pygame.font.Font('Gameplay.ttf', 40)
        self.window = pygame.display.set_mode((800, 595))
        self.texto_0 = self.font.render('Press SPACE To Start!', True, 'white')
        self.texto_1 = self.font.render('Press SPACE To Start!', True, 'grey')
        self.texto2 = self.font.render('Game Title', True, 'white')
        self.clock = pygame.time.Clock()
        self.animation_index = 0
        self.texts = [self.texto_0, self.texto_1]

        pygame.font.init()
        pygame.font.get_init()

    def Init(self):
        while self.menu:

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.menu = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.menu = False

            self.window.blit(self.background.image, self.background.rect)

            if self.animation_index * 1 >= 60:
                self.animation_index = 0

            self.window.blit(self.texts[self.animation_index//30], (125, 443))
            self.animation_index += 1
            self.window.blit(self.texto2, (270, 220))

            pygame.display.update()
            self.clock.tick(60)
