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


    def __init__(self,file,image_width,image_height,cols,rows):
        '''
        Constructor
        '''
        self.baseimage = pygame.image.load(file)#load the image
        self.image_width = image_width
        self.image_height = image_height
        self.cols = cols
        self.rows = rows
        self.subimagewd = self.image_width/self.cols
        self.subimageht = self.image_height/self.rows
        self.subimage = pygame.Rect(0,0,self.subimagewd,self.subimageht)
        self.frameNumber = 0
        self.alphacolor = (0,0,0)#color to be trimmed
        self.sprites = []
        
        for i in range(self.cols*self.rows):
            i+=1#place holder

    def draw(self, xpos, ypos, screen):
        print()#place holder
        