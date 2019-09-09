import pygame
import os, random
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
yellow = 255,255,0
green = 0,155,0

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

def score():
    pass

def timer():
    pass

def main():
    gun_aimImage = pygame.image.load('images/aim_2.png')
    gun_aimImageWidth = gun_aimImage.get_width()
    gun_aimImageHeight = gun_aimImage.get_height()

    gunImage = pygame.image.load("images/gun_1.png")
    gunImageWidth = gunImage.get_width()
    gunImageHeight = gunImage.get_height()

    zombie_1_Images = os.listdir('images/zombie_1')
    zombie_1_Frames = []
    for i in range(len(zombie_1_Images)):
        img = pygame.image.load('images/zombie_1/'+zombie_1_Images[i])
        zombie_1_Frames.append(img)

    zombie_2_Images = os.listdir('images/zombie_2')
    zombie_2_Frames = []
    for i in range(len(zombie_2_Images)):
        img = pygame.image.load('images/zombie_2/' + zombie_2_Images[i])
        zombie_2_Frames.append(img)

    zombieFrames = [zombie_1_Frames,zombie_2_Frames]

    # zombieCount = random.randint(2,5)
    zombiePos = []
    zombieRandomFrames = []
    zombieRect = []
    zombieImageList = []
    zombieImg = img
    colors = []
    zombieCount = 4
    for i in range(zombieCount):
        zombieImgWidth = zombieImg.get_width()
        zombieImgHeight = zombieImg.get_height()
        zombieX = i * (zombieImgWidth + 15)
        zombieY = random.randint(0, height - zombieImgHeight)
        zombiePos.append([zombieX, zombieY])
        rect = pygame.Rect(zombieX, zombieY, zombieImgWidth, zombieImgHeight)
        zombieRect.append(rect)
        zombieFr_1 = random.choice(zombieFrames)
        col = random.randint(1,255),random.randint(1,255),random.randint(1,255)
        colors.append(col)
        zombieRandomFrames.append(zombieFr_1)

    pos = 0

    shotSound = pygame.mixer.Sound('sounds/shot_sound.wav')

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                shotSound.play()
                # print(len(zombieImageList),len(zombieRandomFrames),len(zombieRect))
                for i in range(len(zombieRect)):
                    if zombieRect[i].colliderect(gunAimRect):
                        del zombieRect[i]
                        del zombieImageList[i]
                        del zombieRandomFrames[i]
                        del colors[i]
                        break
                        # zombieFr = random.choice(zombieFrames)
                        # zombieX = random.randint(0, width - zombieImgWidth * 2)
                        # zombieY = random.randint(0, height - zombieImgHeight)

        posx,posy = pygame.mouse.get_pos()
        gunX,gunY = posx - gun_aimImageWidth / 2, posy - gun_aimImageHeight / 2

        screen.fill(white)

        pos += 1
        frame = (pos // 40) % len(zombieRandomFrames)
        for i in range(len(zombieRandomFrames)):
            zombieImg = zombieRandomFrames[i][frame]
            zombieImageList.append(zombieRandomFrames[i])
            pygame.draw.rect(screen,colors[i],zombieRect[i])

            if len(zombieImageList) > len(zombieRandomFrames):
                del zombieImageList[0]

            screen.blit((zombieImg), (zombiePos[i][0], zombiePos[i][1]))

        gunAimRect = pygame.Rect(gunX, gunY, gun_aimImageWidth, gun_aimImageHeight)
        screen.blit(gunImage, (posx, height - gunImageHeight))
        screen.blit(gun_aimImage, (gunX,gunY))

        pygame.display.update()

# main()
homeScreen()