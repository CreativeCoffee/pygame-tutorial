import pygame

pygame.init()

width = 600
height = 800
fps = 60

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("a racing game")
clock = pygame.time.Clock()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        print(event)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
