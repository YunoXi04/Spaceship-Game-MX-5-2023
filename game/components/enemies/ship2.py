import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, LEFT, RIGHT, SCREEN_WIDTH,BULLET_ENEMY_TYPE

class Ship2(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_Y = 6
    SPEED_X = 10
    SHOOTING_INTERVAL = 1000

    def __init__(self, Speed):
        self.image = pygame.transform.scale(ENEMY_2, (self.WIDTH, self.HEIGHT))
        self.shooting_time = 0
        super().__init__(self.image, Speed)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X + self.Speed
            if self.rect.left <= 0:
                self.mov_x = RIGHT
        else:
            self.rect.x += self.SPEED_X+self.Speed
            if self.rect.right >= SCREEN_WIDTH:
                self.mov_x = LEFT


    def update(self, bullet_handler):
        self.move()
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.shoot(bullet_handler)
        
        