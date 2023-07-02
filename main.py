import pygame

# create screen object
screen = pygame.display.set_mode( (300,300) )
# fill screen with a color
color_purple = (160,32,240)
screen.fill(color_purple)
# give it a name
pygame.display.set_caption("Stevie's first game")

# update screen
pygame.display.flip()

# infinite loop for the game to run
running=True
while running:
    # capture events 
    for event in pygame.event.get():
        # check the event type
        if event.type==pygame.QUIT:
            running=False
