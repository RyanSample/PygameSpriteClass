'''


@author: unweaponsinspector
'''
from Sprites import *
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280,720))#deal with it

def main():
    sprite = Sprites()
    sprite.createAnimation("animation", 7, "ninja/flip_0")
    #sprite.createAnimation("animation2", 5, "ninja/die_0")
    sprite.setDelay(50)
    while True:
        screen.fill((0,0,0))
        sprite.playAnimation("animation", 0, 0, screen)
        #sprite.playAnimation("animation2", 140, 140, screen)
        msElapsed = clock.tick(30)#PCMR
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
                
if __name__ == '__main__':
    main()
    
