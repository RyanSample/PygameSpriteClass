'''
Created on May 8, 2015

@author: unweaponsinspector
'''
from Sprites import *
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,720))#deal with it

def main():
    sprite = Sprites("./Data/asteroid.bmp",516,519,9,8)
    while True:
        sprite.draw(screen)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
                
if __name__ == '__main__':
    main()
    
    """currently need to split the spritesheet and then divide it into indiv sprites.
    then create animations then add bugs I mean features."""