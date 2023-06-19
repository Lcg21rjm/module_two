
import random
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, HEART_TYPE


class Heart(PowerUp):
       def __init__(self):
        self.power_image=HEART
        super().__init__( self.power_image,HEART_TYPE)