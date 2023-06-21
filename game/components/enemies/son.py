import random
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Son:
    X_POS_LIST = [100, 800]
    SPEED_X = 10
    SPEED_Y = 10
    INTERVAL = 20

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.is_alive = True
        self.index = 0

    def update(self):
        if self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False

        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.x += self.SPEED_X
        self.rect.y += self.SPEED_Y
