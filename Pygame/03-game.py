import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))

color_1 = 200, 120, 100
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0
screen.fill(white)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen,color,[x,y,w,h]
    pygame.draw.rect(screen,red,(0,0,50,50))

    pygame.draw.circle(screen,red,(100,100),50)

    pygame.display.flip()