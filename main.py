# import and init pygame.
import pygame
pygame.init()

# Variables
width = 600
height = 800
fps = 60
black = (0,0,0)
white = (255,255,255)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("a racing game")
clock = pygame.time.Clock()
player = pygame.image.load("racecar.png")
gameOver = False
x = (width * 0.45)
y = (height * 0.8)
x_change = 0

def displayplayer(x,y):
    window.blit(player, (x,y))


# main game loop
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
    displayplayer(x,y)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
