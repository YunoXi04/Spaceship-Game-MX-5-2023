import pygame 

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, INTRO
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.components.power_ups.new_life import  NewLife
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
        self.power_up_handler = PowerUpHandler()
        self.new_life = NewLife()
        self.number_death = 0
        self.score = 0
        self.score_list = []
        self.life = 50
        self.music()

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay()
        pygame.quit()
        pygame.display.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()    

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.player, self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies, self)
            self.power_up_handler.update(self.player)
            self.new_life.update(self.player)
            self.score = self.enemy_handler.number_enemies_destroyed * 10
            if not self.player.is_alive:
                self.score_list.append(self.score)
                self.draw()
                pygame.time.delay(300)
                self.playing = False
                self.number_death += 1
                

    def draw(self):
        self.draw_background()
        if  self.playing:
            self.clock.tick(FPS)
            self.enemy_handler.draw(self.screen)
            self.player.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.new_life.draw(self.screen)
            self.draw_score()
            life_utils.draw_life(self.life, self.screen)
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        print("xx")
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message("Press ENTER to Start", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect) 
        else:
            best, best_score = text_utils.get_message(f"Best Score: {max(self.score_list)}", 30, WHITE_COLOR, height=SCREEN_HEIGHT//2 - 50)
            text, text_rect = text_utils.get_message("Press ENTER to Restart", 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f"Your Score is: {str(self.score)}", 30, WHITE_COLOR, height=SCREEN_HEIGHT // 2 + 50)
            tries, tries_rect = text_utils.get_message(f"Deads Player: {self.number_death}", 20, WHITE_COLOR)
            tries_rect.topright = (SCREEN_WIDTH - 10, 10)
            self.screen.blit(best, best_score)
            self.screen.blit(text, text_rect) 
            self.screen.blit(score, score_rect)
            self.screen.blit(tries, tries_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f"Your Score is: {self.score}", 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)        

    def reset(self):
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.new_life.reset()
        self.player.reset()

    def music(self):
        pygame.mixer.init() 
        pygame.mixer.music.load(INTRO)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.10)


        
