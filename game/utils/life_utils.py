import pygame

from game.utils.constants import HEARTS


def draw_life(life, screen):
    image = pygame.transform.scale(HEARTS, (20, 20))
    rect = image.get_rect()
    rect.center = (20, 25)
    screen.blit(image, rect)