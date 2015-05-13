'''


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
        
        self.timer = 0
        self.delay = 0
        self.imageList = ''
        self.imageListindex = 0
        self.animations = {}
        self.play = False
        #setter for delay in ms
    def setDelay(self, time):
        self.delay = time
        #returns the current sprite number
    def getCurrentSprite(self):
        return self.imageListindex    
    #function to get the size of the current sprite
    def getCurrentSize(self):
        return self.image.get_rect()
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
        self.play = True
        image_list = self.animations[animation] #get the animation list
       
        if(self.imageListindex < len(image_list)):     
            #still draws 2 frames at the same time
            self.image = image_list[self.imageListindex]
            self.draw(screen, x, y)
            self.imageListindex += 1
        else: # reset the animation
            self.imageListindex = 0 
            self.image = image_list[self.imageListindex]
            self.draw(screen, x, y)
    def pauseAnimation(self):
        self.play = False
    #function to scale an animation. Replaces the animation with a scaled version
    #copy an animation and then scale it if you do not want to rescale #dealwithit           
    def scaleAnimation(self, animation, scale):
        image_list = self.animations[animation]
        index = 0
        for image in image_list:
            rect = image.get_rect()
            new_width = rect.width * scale
            new_height = rect.height * scale
            image_list[index] = pygame.transform.scale(image, (new_width, new_height))
        self.animations[animation] = image_list #replace the image list in the dict with scaled image
            
    def draw(self, screen, x = 0, y = 0):
        rect = self.image.get_rect()
        rect.x = x
        rect.y = y
        if (pygame.time.get_ticks() - self.timer >= self.delay) and self.play == True:
            self.timer = pygame.time.get_ticks()
            screen.blit(self.image,rect)