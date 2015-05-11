'''
Created on May 8, 2015

@author: unweaponsinspector
'''
import os
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
        self.animations = {}
    #create animation takes the number of Frames and 
    #takes a filename up to the number on the animation and then appends the frame number
    #as well as the extension       
    def createAnimation(self, animationName, numberOfFrames, filename):
        dataFolder = 'Data/' #path to Data folder
        Images = []
        for i in range(1, numberOfFrames + 1):
            file = os.path.join(dataFolder, "%s%d.png" %(filename, i))
            print(file)
            self.image = pygame.image.load(file)
            Images.append(self.image)
        self.animations[animationName] =  Images    #add the animation name and the images to the dict
    
    def draw(self, screen, x = 0, y = 0):
        rect = self.image.get_rect()
        rect.x = x
        rect.y = y
        screen.blit(self.image,rect)