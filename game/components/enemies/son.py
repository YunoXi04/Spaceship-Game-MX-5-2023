import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3, SCREEN_HEIGHT

class Son(Enemy):
   WIDTH = 50
   HEIGHT = 60

def __init__(self, Speed):
        self.image = pygame.transform.scale(ENEMY_3, (self.WIDTH, self.HEIGHT))
        self.speed_y = random.randrange(20, 25)
        super(Enemy).__init__(self.image, Speed)
      
def move(self):
        self.rect.y += self.speed_y+self.extra_speed

def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
