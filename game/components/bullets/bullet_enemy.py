import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, BULLET_ENEMY_TYPE, SCREEN_HEIGHT

class BulletEnemy(Bullet):
    WIDTH = 9
    SCREEN_HEIGHT = 32
    SPEED = 10

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.type = BULLET_ENEMY_TYPE
        super().__init__(self.image, self.type, center)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)   

#verificar con cual draw funciona#
    def draw(self, screen):
        screen.blit(self.image, self.rect)         

    def update(self, player):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        super().update(player) 