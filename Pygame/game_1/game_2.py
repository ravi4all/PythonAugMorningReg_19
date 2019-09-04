import pygame
import random

pygame.init()
pygame.mixer.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

color_1 = 200, 120, 100
red = 255, 0, 0
white = 255, 255, 255
black = 0, 0, 0
blue = 0,0,255

pygame.mixer.music.load('StreetFighter.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

snd_1 = pygame.mixer.Sound('punch2.wav')

def score(s):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score : {}".format(s),True,red)
    screen.blit(text, (10,10))

def life(lifeRemaining):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Life Remaining : {}".format(lifeRemaining), True, red)
    screen.blit(text, (200, 10))

def gameOver():
    font_1 = pygame.font.SysFont(None,80)
    text_1 = font_1.render("Game Over",True,black)
    font_2 = pygame.font.SysFont(None,60)
    text_2 = font_2.render("Press Any Key to Start Again",True,black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()

        screen.blit(text_1,(200,100))
        screen.blit(text_2,(100,250))

        pygame.display.update()


def main():
    barWidth = 200
    barHeight = 20
    img = pygame.Surface((barWidth,barHeight))
    img.fill(red)
    barRect = img.get_rect()
    barRect.center  = width/2, height/2
    barRect.y = height - 25
    moveX = 0

    brickSurface = pygame.Surface((width-50,175))
    # brickSurface.fill(white)

    brickWidth = 100
    brickheight = 30

    brickList = []
    brickColors = []
    for row in range(1,6):
        for col in range(9):
            brickX = col * (brickWidth+5)
            brickY = row * (brickheight+5)
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            brickColors.append(color)
            brickList.append(pygame.Rect(brickX,brickY,brickWidth,brickheight))

    ballSurface = pygame.Surface((8,8))
    ballSurface.fill(blue)
    ballRect = ballSurface.get_rect()

    ballRadius = 8
    ballY = barRect.y - ballRadius
    moveBall = False
    ballOnBar = True
    moveBallY = 0
    moveBallX = 0

    FPS = 100
    clock = pygame.time.Clock()

    counter = 0
    lifeRemaining = 3

    while True:
        if ballOnBar:
            ballX = barRect.x + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            moveX = 5
        elif keypressed[pygame.K_LEFT]:
            moveX = -5
        elif keypressed[pygame.K_SPACE]:
            moveBall = True
            ballOnBar = False
        else:
            moveX = 0

        screen.fill(white)
        brickSurface.fill(white)
        screen.blit(brickSurface, (30, 20))
        screen.blit(img,(barRect.x,barRect.y))

        for i in range(len(brickList)):
            pygame.draw.rect(screen,brickColors[i],brickList[i])

        pygame.draw.circle(screen,blue,(ballX,ballY),ballRadius)
        ballRect = pygame.Rect(ballX,ballY,ballRadius,ballRadius)

        if moveBall:
            moveBallY = -3
            moveBallX = 3
            moveBall = False

        ballX += moveBallX
        ballY += moveBallY
        barRect.x += moveX

        for i in range(len(brickList)):
            if brickList[i].colliderect(ballRect):
                del brickList[i]
                moveBallY = 3
                FPS += 5
                counter += 1
                snd_1.play()
                break

        if ballX > width - ballRadius:
            moveBallX = -3
        elif ballX < ballRadius:
            moveBallX = 3
        elif ballY < ballRadius:
            moveBallY = 3
        elif ballRect.colliderect(barRect):
            moveBallY = -3
        elif ballY > height * 2:
            ballOnBar = True
            moveBallX = 0
            moveBallY = 0
            ballY = barRect.y - ballRadius
            lifeRemaining -= 1

        if lifeRemaining == 0:
            gameOver()

        score(counter)
        life(lifeRemaining)

        pygame.display.flip()
        clock.tick(FPS)

main()