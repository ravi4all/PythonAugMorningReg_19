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

img = pygame.image.load("ball_1.png")
bg_img = pygame.image.load("bg_img.png")
bg_img = pygame.transform.scale(bg_img,(width,height))

x = 0
y = 0

moveX = 5
moveY = 5

FPS = 100
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    color = random.choice([red,black,color_1])
    screen.fill(color)


    screen.blit(bg_img,(0,0))
    screen.blit(img,(x,y))

    x += moveX
    y +=  moveY

    if x > width - 150:
        moveX = -5
    elif x < 0:
        moveX = 5
    elif y > height - 150:
        moveY = -5
    elif y < 0:
        moveY = 5

    pygame.display.flip()
    clock.tick(FPS)