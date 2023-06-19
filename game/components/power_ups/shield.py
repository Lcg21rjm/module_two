
import random
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, SHIELD, SHIELD_TYPE


class Shield(PowerUp):
       def __init__(self):
        self.power_image=SHIELD
        super().__init__( self.power_image,SHIELD_TYPE)