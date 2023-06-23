
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEARTS
from game.components.power_ups.shield import Shield


class NewLife(PowerUp):

    INTERVAL_TIME = 700

    def __init__(self):
        self.image = HEARTS
        self.interval_time = 0
        super().__init__(self.image)


    def update(self, player):
        self.interval_time += 1  
        if self.interval_time % self.INTERVAL_TIME == 0:
            self.add_power_up()
            self.interval_time = 0
        for power_up in self.power_ups:
            power_up.update(player)
            if power_up.is_used:
                player.activate_power_up(power_up) 
            if not power_up.is_alive:
                self.remove_power_up(power_up)

    def draw(self, screen):
        for  power_up in self.power_ups:
            power_up.draw(screen)


    def add_power_up(self):
        self.power_ups.append(Shield())

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)

    def reset(self):
        self.power_ups = []
        self.interval_time = 0        