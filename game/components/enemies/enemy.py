import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, SCREEN_WIDTH, SPACESHIP,SCREEN_HEIGHT,ENEMY_2

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGTH = 60
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0:"left", 1:"rigth"}
    IMAGE_ENEMY1 = {0:ENEMY_1, 1:ENEMY_2}

    def __init__(self) :
        self.image = self.IMAGE_ENEMY1[random.randint(0,1)]
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS_LIST[random.randint(0,10)]
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(10,150)
        self.index = 0
        self.type = "enemy"
        self.shooting_time = random.randint(30, 50)


    def update(self, ships,game):
        
        self.rect.y += self.speed_y 
        self.shoot(game.bullet_manager)

        if self.movement_x == "left":
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

        

    def draw(self,screen ):
        screen.blit(self.image, (self.rect.x, self.rect.y) )
    
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == "rigth") or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH ):
            self.movement_x = "left"
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == "left") or (self.rect.x <= 10 ) :
            self.movement_x = "rigth"
            self.index = 0


    def shoot(self,bullet_Manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_Manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)

  