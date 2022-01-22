import pygame

pygame.init() #init

#create the screen

screen = pygame.display.set_mode((800,600))

#Title and Icon

pygame.display.set_caption("DayLite")

icon = pygame.image.load('zombie1.png')
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    screen.fill((0,0,255))
    pygame.display.update()