import pygame_menu
import math
import random
import time
import sys
from tkinter.font import names

import pygame
from pygame import mixer


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Main Menu
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
#Set Time Clock

mainClock = pygame.time.Clock()


# Background
background = pygame.image.load('backgroundss1.png')




# Sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("DayLite")
icon = pygame.image.load('zombie1.png')
pygame.display.set_icon(icon)

# Player
class Player:
    def __init__(self, name, health, posx,posy):
        self.img = self.IMG
        self.name = name
        self.health = health
        self.posx = posx
        self.posy = posy

    def __str__(self):
        return self.name

playerImg = pygame.image.load('user.png')
playerImg = pygame.transform.scale(playerImg, (100,100))
playerX = 370
playerY = 277
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemy = pygame.image.load('zombie.png')
    enemy = pygame.transform.scale(enemy, (100,100))
    enemyImg.append(enemy)
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Score

score_value = 0
health_value = 0
tower_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

#def player_jump():
 #   playerY +=5


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_health(x, y):
    health = font.render("Health : " + str(health_value), True, (255, 255, 255))
    screen.blit(health, (x, y))

def show_tower(x, y):
    tower = font.render("Tower Power : " + str(tower_value), True, (255, 255, 255))
    screen.blit(tower, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))




# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((173, 216, 230))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                #player_jump(True) might implement
                playerX_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
      #  collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        #if collision:
      #      score_value += 1
      #      enemyX[i] = random.randint(0, 736)
      #      enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(textX, testY)
    show_health(textX+200, testY)
    show_tower(textX+400, testY)
    pygame.display.update()