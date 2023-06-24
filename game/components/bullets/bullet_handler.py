from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer

class BulletHandler:
    def __init__(self):
        self.bullets = []
        
    def update(self, player, enemies, game):
        for bullet in self.bullets:
            if isinstance(bullet, BulletEnemy):
                bullet.update(player)
                print(game.life)
            elif isinstance(bullet, BulletPlayer):
                for enemy in enemies:
                    bullet.update(enemy)   
                if not bullet.is_alive:
                    self.remove_bullet(bullet)       
   

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet_type, center):
        if bullet_type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif bullet_type == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))    

    def remove_bullet(self, bullet):
        if not bullet.is_alive:
            self.bullets.remove(bullet)

    def reset(self):
        self.bullets = []    
   


