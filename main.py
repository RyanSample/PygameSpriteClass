'''
Created on May 8, 2015

@author: unweaponsinspector
'''
from Sprites import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,720))#deal with it

def main():
    sprite = Sprites("./Data/asteroid.bmp",516,519,9,8)
    while True:
        sprite.draw(screen)
        pygame.display.update()
    pygame.quit()
if __name__ == '__main__':
    main()