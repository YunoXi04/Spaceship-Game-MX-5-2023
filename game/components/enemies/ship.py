import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, RIGHT, LEFT, SCREEN_WIDTH, BULLET_ENEMY_TYPE, SCREEN_HEIGHT

class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED_Y =  10
    SPEED_X = 5
    INTERVAL = 10
    SHOOTING_TIME = 1000

    
    def __init__(self, Speed):
        self.image = pygame.transform.scale(ENEMY_1, (self.WIDTH, self.HEIGHT))
        self.cont = 0
        self.shooting_time = 0
        
        super().__init__(self.image, Speed)

    def move(self):   
        self.rect.y += self.SPEED_Y + self.Speed
        if self.mov_x == LEFT:
           self.rect.x -= self.SPEED_X + self.Speed
        if self.cont > self.INTERVAL or self.rect.left <= 0:
            self.mov_x = RIGHT
            self.cont = 0 
        else:
            self.rect.x += self.SPEED_X + self.Speed
        if self.cont > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
            self.mov_x = LEFT
            self.cont = 0
        self.cont += 1

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)
        
    
    def update(self, bullet_handler):
        self.move()
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.shoot(bullet_handler)
        
    
        
                     

