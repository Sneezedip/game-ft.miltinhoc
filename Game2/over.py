from background import Background
import pygame


class Over():
    def __init__(self):
        from platform import current_score
        self.over = True
        self.background = Background('background2.png')
        self.font = pygame.font.Font('Gameplay.ttf', 40)
        self.window = pygame.display.set_mode((800, 595))
        self.texto_1 = self.font.render(
            f'Your Score: {current_score}', True, 'white')
        self.texto_0 = self.font.render(
            'Press SPACE To Restart!', True, 'white')
        self.texto_2 = self.font.render(
            'Press SPACE To Restart!', True, 'grey')
        self.animation_index = 0
        self.texts = [self.texto_0, self.texto_2]
        self.clock = pygame.time.Clock()

        pygame.font.init()
        pygame.font.get_init()

    def Init(self):
        global janela_aberta
        while self.over:

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.over = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.over = False
                janela_aberta = True

            self.window.blit(self.background.image, self.background.rect)
            self.window.blit(self.texto_1, (225, 220))

            if self.animation_index * 1 >= 60:
                self.animation_index = 0

            self.window.blit(self.texts[self.animation_index//30], (100, 443))
            self.animation_index += 1

            pygame.display.update()
            self.clock.tick(60)
