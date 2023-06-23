import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_4, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE


class Father(Enemy):
    WIDTH = 50
    HEIGHT = 50
    POS_X = [-WIDTH, SCREEN_WIDTH + WIDTH]
    SHOOTING_INTERVAL = 30

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_4,(self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.POS_X)
        self.rect.y = random.randint(0, SCREEN_HEIGHT // 2 - self.HEIGHT)
        self.speed_x = 20
        self.is_alive = True
        self.shooting_timer = 0
        self.start = True
        self.is_destroyed = False

    def update(self, player_pos,bullet_handler):
        self.move(player_pos)
        self.shoot(bullet_handler)
        self.shooting_timer += 1
        if self.shooting_timer >= self.SHOOTING_INTERVAL:
            self.shoot(bullet_handler)
            self.shooting_timer = 0

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
   
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)

                