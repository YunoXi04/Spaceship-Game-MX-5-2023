import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Ship2(Enemy):
    WIDTH = 70
    HEIGHT = 90
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)