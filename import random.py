import random

from game.utils.constants import HEART, SHIELD


power_ups=[]
power_image={0:SHIELD, 1:HEART}
image = power_image[random.randint(0,1)]
power_ups.append(image)




if image == SHIELD:
    print ("hola000000000000000000000000000000")
    print(power_ups)
elif image == HEART:
    print ("hola111111111111111111111111")
    print(power_ups)

    
