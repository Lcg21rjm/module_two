import os
import random
import pygame
from pygame.sprite import Sprite
import game
from game.components.bullets.bullet import Bullet
from game.utils.constants import  DEFAULT_TYPE, IMG_DIR, SCREEN_WIDTH, SPACESHIP, SCREEN_HEIGHT

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = "player"
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

    def update(self,game,user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()

        elif user_input[pygame.K_DOWN]:
            self.move_down()

        elif user_input[pygame.K_SPACE]:
            self.shoot(game)
        
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.x <= 0:
             self.rect.x = SCREEN_WIDTH     
    
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.x > SCREEN_WIDTH :
            self.rect.right = 0    
    
    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
        if self.rect.y < 0:
             self.rect.y = 0 
        
    
    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        if self.rect.y >= self.Y_POS:
            self.rect.y = self.Y_POS + 20

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)
        
        
        

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def set_image(self, size =(SHIP_WIDTH, SHIP_HEIGTH), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
        

