
from game.components.bullets.bullet_manager import BulletManager
from game.components.power_ups.heart import Heart
from game.components.power_ups.bullet import PowerBullet
from game.components.power_ups.power_up import PowerUp
#from game.components.power_ups.shield import Shield
import random

import pygame
from game.components.power_ups.shield import Shield

from game.utils.constants import BALA_TYPE, HEART, HEART_TYPE, SHIELD, SPACESHIP_SHIELD


from game.utils.constants import HEART, SHIELD, SHIELD_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)
        self.random_power = random.randint(1,3)
        

    def update(self, game):
        current_time = pygame.time.get_ticks()
        self.random_power = random.randint(1,2)

        if len(self.power_ups) == 0 and current_time >= self.when_appears :
            self.generate_power_up(game)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if  game.player.rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    if game.player.power_up_type == SHIELD_TYPE:
                        game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                        game.player.set_image((65, 75), SPACESHIP_SHIELD)
                        self.power_ups.remove(power_up)
                    elif game.player.power_up_type == HEART_TYPE:
                            game.deat_count = 0
                            self.power_ups.remove(power_up)
                    elif game.player.power_up_type == BALA_TYPE:
                         self.power_ups.remove(power_up)

                         
                        

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self, game):
        if self.random_power == 1:
            power= Shield()
        elif self.random_power == 2:
            power = Heart()
        elif self.random_power == 3: 
            power = PowerBullet()
        
        self.power_ups.append(power)
        self.when_appears += random.randint(5000, 10000) 
        
    

    def reset(self):
        self.power_ups = []