
import random

import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BALA_POWER, BALA_TYPE


class PowerBullet(PowerUp):
       def __init__(self):
        self.power_image= BALA_POWER
        self.bala_power = pygame.transform.scale(BALA_POWER,(20,20))
        super().__init__( self.bala_power,BALA_TYPE)