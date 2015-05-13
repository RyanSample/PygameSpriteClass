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

    def __init__(self):
        'self.image = pygame.image.load(filename)   '     
        
        #self.image.convert()#used for non bmp images. runs faster when not used
        
        self.image =''
        self.delay = 50
        self.timer = 0
        self.delay = 0
        self.animations = {}
        #setter for delay in ms
    def setDelay(self, time):
        self.delay = time
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
            Images.append(self.image)#add to images list
        self.animations[animationName] =  Images    #add the animation name and the image list to the dict
    def setTransparency(self, animation, r, g, b):
        color = (r,g,b)
        image_list = self.animations[animation] #get the image list from the animations dict
        for image in image_list:
            self.image.set_colorkey(color)#set the colorkey see pygame's Surface docs
    #need to implement 
    def playAnimation(self, animation, x, y, screen):
        image_list = self.animations[animation] #get the animation list
        
        for image in image_list:
            self.image = image
            self.draw(screen, x, y)#still draws 2 frames at the same time
            
    def draw(self, screen, x = 0, y = 0):
        rect = self.image.get_rect()
        rect.x = x
        rect.y = y
        if (pygame.time.get_ticks() - self.timer >= self.delay):
            self.timer = pygame.time.get_ticks()
            screen.blit(self.image,rect)