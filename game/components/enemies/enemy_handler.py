from game.components.enemies.ship import Ship

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self):
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) <2:
           self.enemies.append(Ship())  

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)            

