import pygame
pygame.init ()
W = 500
H = 500
screen = pygame.display.set_mode ((W,H))
while (True):
    for event in pygame.event.get ():
       if event.type == pygame.QUIT:
            pygame.quit ()
    screen.fill ("white")
    pygame.display.update ()
