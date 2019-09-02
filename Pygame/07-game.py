import pygame
import random

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

color_1 = 200, 120, 100
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0

x = 0
y = 0

moveX = 0

# rect = pygame.Rect(x,y,50,50)

img = pygame.Surface((200,20))
img.fill(red)
rect_1 = img.get_rect()
rect_1.center  = width/2, height/2
rect_1.y = height - 25
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_RIGHT]:
        moveX = 1
    elif keypressed[pygame.K_LEFT]:
        moveX = -1
    else:
        moveX = 0

    color = random.choice([red,black,color_1])
    screen.fill(white)
    screen.blit(img,(rect_1.x,rect_1.y))

    rect_1.x += moveX

    if rect_1.right > width:
        moveX = -1
    elif rect_1.left < 0:
        moveX = 1

    pygame.display.flip()