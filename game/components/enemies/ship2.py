import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, LEFT, RIGHT, SCREEN_WIDTH

class Ship2(Enemy):
    WIDTH = 70
    HEIGHT = 90
    SPEED_Y = 6
    SPEED_X = 20

    def __init__(self, Speed):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, Speed)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X+self.Speed
            if self.rect.left <= 0:
                self.mov_x = RIGHT
        else:
            self.rect.x += self.SPEED_X+self.Speed
            if self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT


    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()