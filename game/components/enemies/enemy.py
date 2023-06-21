import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT, BULLET_ENEMY_TYPE

class Enemy:
    
    Y_POS_INICIAL = -60
    MOV_X = [RIGHT, LEFT]
    Speed = 0
    SPEED_Y = 0
    SPEED_X = 0
    SHOOTING_TIME = 30


    def __init__(self, image, Speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS_INICIAL
        self.is_alive = True
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.shooting_time = 0
        self.is_destroyed = False
        self.Speed = Speed

    def update(self, bullet_handler):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
            self.shooting_time += 1
            self.shoot(bullet_handler)
            self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y += self.SPEED_Y
        if self.MOV_X == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.left <= 0:
                self.MOV_X = RIGHT
                self.index = 0
        
        else:
            self.rect.x += self.SPEED_X 
            if self.index > self.INTERVAL or self.rect.right >= SCREEN_WIDTH:
                self.MOV_X = LEFT
        self.index += 1

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)


