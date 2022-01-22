import math
import random

import pygame

from pygame import mixer

#Background
background = pygame.image.load("nature-8597.png")
pygame.init() #init


# Sound
#mixer.music.load("")
#mixer.music.play(-1)

#Create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon

pygame.display.set_caption("DayLite")

icon = pygame.image.load('zombie1.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('user.png')
playerX= 30
playerY = 50
playerY
def player(x,y): 
    screen.blit(playerImg,(playerX,playerY))


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    #RGB red green blue
    screen.fill((0,0,255))

    player(playerX,playerY)
    pygame.display.update() #this is important for game to display! 