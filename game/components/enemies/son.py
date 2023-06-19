import random
from game.utils.constants import SCREEN_HEIGHT

class Son:
    X_POS_LIST = [100, 400, 600, 800]
    SPEED_Y = 10
    SPEED_X = 0
    INTERVAL = 100

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = 0
        self.is_alive = True
        self.index = 0

    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False

        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y += self.SPEED_Y
        self.rect.x = self.SPEED_X