import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGHT

class Son:
    
    X_POS_LIST = [150, 450, 550, 650, 850]
    Y_POS = 0
    SPEED_X = 2
    SPEED_Y = 2
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100


    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
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