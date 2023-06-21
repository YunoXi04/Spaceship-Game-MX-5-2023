import pygame 

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.utils import text_utils
from game.utils import life_utils



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.number_deadth = 0
        self.score = 0

    def run(self):
        # Game loop: events - update - draw
        self.running= True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(300)
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN and not self. playing:
                self.playing = True
                self.reset()    

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.player, self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score[self.number_deadth] = self.enemy_handler.number_enemies_destroyed * 10
            if not self.player.is_alive:
                self.draw()
                pygame.time.delay(300)
                self.playing = False
                self.number_deadth += 1
                self.scores.append(0)

    def draw(self):
        self.draw_background()
        if  self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.enemy_handler.draw(self.screen)
            self.player.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.draw_score()
            life_utils.draw_ñife(self.player.life.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_deadth == 0:
            text, text_rect = text_utils.get_message("Press any Key to Start", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect) 
        else:
            best, best_score = text_utils.get_message(f"Best Score: {max(self.score)}", 30, WHITE_COLOR, height=SCREEN_HEIGHT//2 - 50)
            text, text_rect = text_utils.get_message("Press any Key to Restart", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f"Your Score is: {self.score}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 50)
            tries, tries_rect = text_utils.get_message(f"Deads: {self.number_deadth}", 20, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 50)
            self.screen.blit(best, best_score)
            self.screen.blit(text, text_rect) 
            self.screen.blit(score, score_rect)
            self.screen.blit(tries, tries_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f"Your Score is: {self.score}", 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)        

    def reset(self):
        self.player.rest()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        
