
import random

import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, HEART_TYPE, VIDA


class Heart(PowerUp):
       def __init__(self):
        self.power_image= VIDA
        self.vida = pygame.transform.scale(VIDA,(20,20))
        super().__init__( self.vida,HEART_TYPE)