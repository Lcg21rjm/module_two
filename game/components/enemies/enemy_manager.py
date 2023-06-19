import os
import random
import time

import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import IMG_DIR, SHIELD_TYPE





class EnemyManager:
    
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()
        self.type = "enemy"
        

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies,game)

            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    SOUND = pygame.mixer_music.load(os.path.join(IMG_DIR,'Other/explosion.wav'))
                    SOUND = pygame.mixer.music.play(1)
                    game.deat_count += 1
                    if game.deat_count >= 3:
                        game.playing = False
                        pygame.time.delay(1000)
                        break
                self.enemies.remove(enemy)
            


    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1 or time.time() - self.last_enemy_time >= 3  :
            self.SPEED_Y = random.randint(1,5)
            self.SPEED_X = random.randint(1,8)
            enemy = Enemy()
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()

    def reset(self):
        self.enemies=[]
    
    
            

    