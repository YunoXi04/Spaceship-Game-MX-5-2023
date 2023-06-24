import pygame
import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3, SCREEN_HEIGHT, BULLET_ENEMY_TYPE

class Son(Enemy):
   WIDTH = 50
   HEIGHT = 60
   SHOOTING_TIME = 1000

   def __init__(self, Speed):
        self.image = pygame.transform.scale(ENEMY_3, (self.WIDTH, self.HEIGHT))
        self.speed_y = random.randrange(20, 25)
        self.shooting_timer = 0
        super().__init__(self.image, Speed)

   def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
        self.shooting_timer += 1
        if self.shooting_timer >= self.SHOOTING_TIME:
            self.shoot(bullet_handler)
            self.shooting_timer = 0

   def move(self):
        self.rect.y += self.speed_y + self.Speed

 
          