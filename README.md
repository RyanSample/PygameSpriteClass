# PygameSpriteClass
A class that divides a sprite sheet into smaller images and then animates that sprite sheet. Made specifically for pygame written in Python
Documentation:
This sprite class reads presplit(png files) sprites from a Data file created by the user.

After instantiation the user can create animations by calling createAnimation() which takes a name, the number of files and the name of the animation range before the frame number and the file extension

To set delay simply call Sprites.setDelay(time) time is a decimal in miliseconds

To play an animation call Sprites.setDelay("animation_name", x, y, surface) surface is generally the screen and I cannot guarantee that the animation will play on another surface

to pause an animation simply call Sprites.pauseAnimation()

Sprites.setTransparency("animation name", r, g, b) will set the transparency for the selected color to the background. Or just get your artist to put alpha around the image to be animated(much more accurate)

Getters:

getCurrentSprite() returns the frame in the animation being run

getCurrentSize() returns a rectangle from the currently drawn image with x,y,width,height

Naming Conventions:

This is very important. This Sprites class expects all images in an animation to start out with the same name before a number followed by a .png      example "flip_0"[1-7].png 	is how the animations are labeled in the flip animation. 

ToDo:

Fix Framerate Bug:
this bug occurs when the Delay is set too high. It causes the image to become choppy and in some cases such as really high delay times it will not display an image at all.
