import pygame

pygame.init()

# screen width - 1000
# screen height - 500
screen = pygame.display.set_mode((1000,500))

# colors - rgb (red,green,blue)
# min - 0
# max - 255
color_1 = 200,120,100
red = 255,0,0
white = 255,255,255
black = 0,0,0
screen.fill(white)

# to update the screen
pygame.display.flip()