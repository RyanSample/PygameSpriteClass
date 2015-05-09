'''
Created on May 8, 2015

@author: unweaponsinspector
'''
import pygame
import sysconfig

pygame.init()

class Sprites(object):
    '''
    classdocs
    '''

    def __init__(self,filename,width,height,columns,rows):
        self.image = pygame.image.load(filename)        
        self.width = width
        self.height = height
        #self.image.convert()#used for non bmp images. runs faster when not used
        self.cols = columns
        self.rows = rows
        #need to get the size of the individual 
        self.sprite_height = self.height // self.rows #// operator makes sure that we dont have decimal
        self.sprite_width = self.width // self.cols
    #def split_sheet(self):
        
        
    def draw(self, screen, x = 0, y = 0):
        rect = self.image.get_rect()
        rect.x = x
        rect.y = y
        screen.blit(self.image,rect)