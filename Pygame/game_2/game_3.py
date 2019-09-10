import pygame
import os, random
from pygame.locals import *
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
yellow = 255,255,0
green = 0,155,0

zombie_1_Images = os.listdir('images/zombie_1')
zombie_1_Frames = []
for i in range(len(zombie_1_Images)):
    img = pygame.image.load('images/zombie_1/' + zombie_1_Images[i])
    zombie_1_Frames.append(img)

zombie_2_Images = os.listdir('images/zombie_2')
zombie_2_Frames = []
for i in range(len(zombie_2_Images)):
    img = pygame.image.load('images/zombie_2/' + zombie_2_Images[i])
    zombie_2_Frames.append(img)

zombieFrames = [zombie_1_Frames, zombie_2_Frames]

def homeScreen():
    bg_img = pygame.image.load("images/bg.jpg")
    font_1 = pygame.font.Font('fonts/font_1.ttf',70)
    text_1 = font_1.render('Zombie Attack',True,white)
    font_2 = pygame.font.Font('fonts/font_1.ttf',40)
    text_2 = font_2.render('Press Any Key to Start Game',True,red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                main()

        screen.blit(bg_img, (0,0))
        screen.blit(text_1,(100,100))
        screen.blit(text_2,(50,250))

        pygame.display.update()

def gameOver():
    pass

def score(s):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score : {}".format(s), True, red)
    screen.blit(text, (400, 10))

def timer(t):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Time Left : {}".format(t), True, red)
    screen.blit(text, (10, 10))

def zombies():
    zombieCount = random.randint(2,6)
    zombiePos = []
    zombieRandomFrames = []
    zombieRect = []
    zombieImg = img
    zombieImg = pygame.transform.scale(zombieImg, (150, 190))
    for i in range(zombieCount):
        zombieImgWidth = zombieImg.get_width()
        zombieImgHeight = zombieImg.get_height()
        zombieX = i * (zombieImgWidth + 15)
        # zombieY = random.randint(0, height - zombieImgHeight)
        zombieY = height - zombieImgHeight - 20
        zombiePos.append([zombieX, zombieY])
        rect = pygame.Rect(zombieX, zombieY, zombieImgWidth, zombieImgHeight)
        zombieRect.append(rect)
        zombieFr_1 = random.choice(zombieFrames)
        zombieRandomFrames.append(zombieFr_1)

    return zombieRandomFrames,zombiePos,zombieRect

def main():
    game_bg = pygame.image.load("images/game_bg.png")
    gun_aimImage = pygame.image.load('images/aim_2.png')
    gun_aimImageWidth = gun_aimImage.get_width()
    gun_aimImageHeight = gun_aimImage.get_height()

    gunImage = pygame.image.load("images/gun_1.png")
    gunImageWidth = gunImage.get_width()
    gunImageHeight = gunImage.get_height()

    zombieRandomFrames,zombiePos,zombieRect = zombies()
    counter = 0
    pos = 0

    shotSound = pygame.mixer.Sound('sounds/shot_sound.wav')

    seconds = 30
    pygame.time.set_timer(USEREVENT, 1000)

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                shotSound.play()
                for i in range(len(zombieRect)):
                    if zombieRect[i].colliderect(gunAimRect):
                        counter += 1
                        del zombieRect[i]
                        del zombieRandomFrames[i]
                        del zombiePos[i]
                        break

        posx,posy = pygame.mouse.get_pos()
        gunX,gunY = posx - gun_aimImageWidth / 2, posy - gun_aimImageHeight / 2

        screen.blit(game_bg,(0,0))

        if len(zombieRandomFrames) == 0:
            zombieRandomFrames, zombiePos, zombieRect = zombies()

        pos += 1
        frame = (pos // 40) % len(zombieRandomFrames)

        for j in range(len(zombieRandomFrames)):
            zombieImg = zombieRandomFrames[j][frame]
            zombieImg = pygame.transform.scale(zombieImg,(150,190))
            screen.blit((zombieImg), (zombiePos[j][0], zombiePos[j][1]))

        gunAimRect = pygame.Rect(gunX, gunY, gun_aimImageWidth, gun_aimImageHeight)
        screen.blit(gunImage, (posx, height - gunImageHeight))
        screen.blit(gun_aimImage, (gunX,gunY))
        timer(seconds)
        score(counter)
        pygame.display.update()

# main()
homeScreen()