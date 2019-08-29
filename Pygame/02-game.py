import pygame

pygame.init()

screen = pygame.display.set_mode((1000,500))

color_1 = 200,120,100
red = 255,0,0
white = 255,255,255
black = 0,0,0
screen.fill(white)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # it will quit pygame
            pygame.quit()
            # it will quit python
            quit()

    pygame.display.flip()