# import and init pygame.
import pygame
import time
import random
pygame.init()

# Variables
width = 800
height = 600
fps = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("a racing game")
clock = pygame.time.Clock()
player = pygame.image.load("racecar.png")
playerwidth = 73

def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(window, color, [blockx, blocky, blockw, blockh])

def displayplayer(x,y):
    window.blit(player, (x,y))

def textObjects(text, font):
    txtSurf = font.render(text, True, black)
    return txtSurf, txtSurf.get_rect()

def gameovermsg(text):
    largetxt = pygame.font.Font('Raleway-Bold.ttf', 80)
    TextSurf, TextRect = textObjects(text, largetxt)
    TextRect.center = ((width / 2), (height / 2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    main()

def playerlose():
    gameovermsg('You Crashed!')

# main game loop
def main():
    # local vars
    gameOver = False
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0
    blockstartingpositionX = random.randrange(0, width)
    blockstartingpositionY = -600
    blockspeed = 7
    blockwidth = 100
    blockheight = 100

    # is game running?
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
            print(event)
        x += x_change
        window.fill(white)
        blocks(blockstartingpositionX, blockstartingpositionY, blockwidth, blockheight, red)
        blockstartingpositionY += blockspeed
        displayplayer(x,y)
        if x > width - playerwidth or x < 0:
            print("Out of Bounds!")
            playerlose()
        if blockstartingpositionY > height:
            blockstartingpositionY = 0 - blockheight
            blockstartingpositionX = random.randrange(0, width)
        if y < blockstartingpositionY+blockheight:
            print("Y Cross")
            if x > blockstartingpositionX and x < blockstartingpositionX + blockwidth or x + playerwidth > blockstartingpositionX and x + playerwidth < blockstartingpositionX + blockwidth:
                print("X Cross")
                playerlose()

        # update screen and fps.
        pygame.display.update()
        clock.tick(fps)

main()
pygame.quit()
quit()
