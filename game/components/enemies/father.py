import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_4, SCREEN_WIDTH, SCREEN_HEIGHT

class Father(Enemy):
    WIDHT = 50
    HEIGHT = 50
    POS_X = [-WIDHT, SCREEN_WIDTH+WIDHT]

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_4, (self.WIDHT, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X[random.randrange(0, 1)]
        self.rect.y = random.randint(0, SCREEN_HEIGHT // 2 - self.HEIGHT)
        self.speed_x = 20
        self.is_alive = True
        self.shooting_time = 0
        self.start = True
        self.is_destroyed = False

    def update(self, player_pos,bullet_handler):
        self.move(player_pos)
        self.shoot(bullet_handler)
        self.shooting_time += 1

    def move(self, player_pos):
        if self.start:
            if self.rect.x < SCREEN_WIDTH // 2:
                self.rect.x += self.speed_x
            elif self.rect.x > SCREEN_WIDTH // 2:
                self.rect.x -= self.speed_x
            else:
                self.start = False
                self.speed_x = 10
        else:
            if player_pos.x > self.rect.x:
                self.rect.x += self.speed_x
            elif player_pos.x < self.rect.x:
                self.rect.x -= self.speed_x