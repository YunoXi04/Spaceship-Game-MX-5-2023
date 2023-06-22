import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, BULLET_ENEMY_TYPE

class Enemy:
    
    y_pos_inicial = -60
    mov_x = [RIGHT, LEFT]
    Speed = 10
    SPEED_Y = 10
    SPEED_X = 10
    SHOOTING_TIME = 30


    def __init__(self, image, Speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = self.y_pos_inicial
        self.is_alive = True
        self.mov_x = random.choice(self.mov_x)
        self.index = 0
        self.shooting_time = 0
        self.is_destroyed = False
        self.Speed = Speed

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
            self.shoot(bullet_handler)
            self.shooting_time += 1
            self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        pass

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)

    def get_damage(self):
        self.is_alive = False
        self.is_destroyed = True              


