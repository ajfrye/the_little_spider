import pygame
screen=pygame.display.set_mode((300,300))
screen.fill((160,32,240))
pygame.display.flip()
running=True
pygame.display.set_caption("Stevie's first game")
while running: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
