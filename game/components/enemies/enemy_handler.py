from game.components.enemies.ship import Ship
from game.components.enemies.ship2 import Ship2
from game.components.enemies.son import Son
from game.components.enemies.father import Father

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.Speed = 10
        self.cont = 1
        self.number_enemies_destroyed = 0

    def update(self, player, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            self.check_colisions(enemy, player)
            enemy.update(player, bullet_handler)
            if enemy.is_destroyed:
                self.number_enemies_destroyed += 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if self.cont % 100 == 0:
            self.enemies.append(Ship2(self.Speed))
            
        if self.cont % 100 == 0:
            self.enemies.append(Ship(self.Speed))

        if self.cont % 400 == 0:
            self.enemies.append(Son(self.Speed)) 

        if self.cont % 600 == 0:
            self.enemies.append(Father(self.Speed))      
        for enemy in self.enemies:
                enemy.Speed = self.Speed
        self.cont += 1        

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)   

    def check_colisions(self, enemy, player):
        if enemy.rect.colliderect(player.rect):
            enemy.is_alive = False
            player.get_damage(10)

    def reset(self):  
        self.enemies = [] 
        self.number_enemies_destroyed = 0 
        self.Speed = 0
        self.cont = 1
            


