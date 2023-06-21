import pygame

from game.utils.constants import HEARTS


def draw_life(life, screen):
    for i in range(0, life//10):
        image = pygame.transform.scale(HEARTS, (20, 20))
        rect = image.get_rect()
        rect.center = (20*(i+1)+5, 25)
        screen.blit(image, rect)