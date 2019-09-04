import pygame
import os
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
yellow = 255,255,0

def homeScreen():
    pass

def gameOver():
    pass

def score():
    pass

def timer():
    pass

def main():
    gun_aimImage = pygame.image.load('images/aim_2.png')
    gun_aimImageWidth = gun_aimImage.get_width()
    gun_aimImageHeight = gun_aimImage.get_height()

    zombie_1_Images = os.listdir('images/zombie_1')
    zombie_1_Frames = []
    for i in range(len(zombie_1_Images)):
        img = pygame.image.load('images/zombie_1/'+zombie_1_Images[i])
        zombie_1_Frames.append(img)

    pos = 0

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        posx,posy = pygame.mouse.get_pos()
        screen.fill(white)

        pos += 1

        screen.blit(gun_aimImage,(posx - gun_aimImageWidth/2,posy - gun_aimImageHeight/2))

        frame = (pos // 40) % len(zombie_1_Frames)
        # print(frame)
        screen.blit(zombie_1_Frames[frame], (100,100))

        screen.blit(zombie_1_Frames[frame], (300, 100))

        screen.blit(zombie_1_Frames[frame], (500, 100))

        pygame.display.update()

main()