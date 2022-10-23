from random import randint
from player import Player
from background import Background
from obstacle import Obstacle, ObstacleFactory
from over import Over
from menu import Menu
import pygame

score = 0
current_score = score
screen_w = 800
screen_h = 595

janela_aberta = True

janela = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Square 2.0")

clock = pygame.time.Clock()

pygame.font.init()
pygame.font.get_init()
# font = pygame.font.SysFont('freesans', 30, True)
font = pygame.font.Font('Gameplay.ttf', 20)

player = pygame.sprite.GroupSingle()
player.add(Player(5, screen_w))

obstacle_group = pygame.sprite.Group()

obstacle_timer = pygame.USEREVENT + 1
obstacle_timer_speed = 1500
pygame.time.set_timer(obstacle_timer, obstacle_timer_speed)

background = Background('background.png')

ob = ObstacleFactory(screen_w)


def collisions():
    obs = pygame.sprite.spritecollide(player.sprite, obstacle_group, False)

    for obstacle in obs:
        player.sprite.damage(obstacle.damage)
        obstacle.remove()


menu = Menu()
menu.Init()

while janela_aberta:

    texto = font.render(f'Score: {score}', True, 'white')
    texto2 = font.render(f'Vida : {player.sprite.hp}', True, 'white')

    janela.blit(background.image, background.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        if event.type == obstacle_timer:
            obstacle_group.add(ob.get_obstacle())
            obstacle_group.add(ob.get_obstacle())

    janela.blit(texto, (5, 5))
    janela.blit(texto2, (5, 50))

    player.draw(janela)
    player.update()

    obstacle_group.draw(janela)
    obstacle_group.update()

    collisions()

    pygame.display.update()
    clock.tick(60)
