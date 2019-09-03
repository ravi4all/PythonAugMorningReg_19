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
blue = 0,0,255

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
    brickSurface.fill(white)

    brickWidth = 100
    brickheight = 30

    brickList = []
    brickColors = []
    for row in range(5):
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

    while True:
        if ballOnBar:
            ballX = barRect.x + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            moveX = 1
        elif keypressed[pygame.K_LEFT]:
            moveX = -1
        elif keypressed[pygame.K_SPACE]:
            moveBall = True
            ballOnBar = False
        else:
            moveX = 0

        screen.fill(white)
        screen.blit(img,(barRect.x,barRect.y))
        screen.blit(brickSurface,(30,20))

        for i in range(len(brickList)):
            pygame.draw.rect(brickSurface,brickColors[i],brickList[i])

        pygame.draw.circle(screen,blue,(ballX,ballY),ballRadius)
        ballRect = pygame.Rect(ballX,ballY,ballRadius,ballRadius)

        if moveBall:
            moveBallY = -1
            moveBallX = 1
            moveBall = False

        ballX += moveBallX
        ballY += moveBallY
        barRect.x += moveX

        if ballX > width - ballRadius:
            moveBallX = -1
        elif ballX < ballRadius:
            moveBallX = 1
        elif ballY < ballRadius:
            moveBallY = 1
        elif ballRect.colliderect(barRect):
            moveBallY = -1
        elif ballY > height * 2:
            ballOnBar = True
            moveBallX = 0
            moveBallY = 0
            ballY = barRect.y - ballRadius

        pygame.display.flip()

main()