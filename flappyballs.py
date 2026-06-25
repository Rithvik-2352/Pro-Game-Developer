import pygame
from shapes import Rectangle
from shapes import Circle
pygame.init ()
W = 500
H = 500
screen = pygame.display.set_mode ((W,H))
c1=Circle (250,250,100,"blue")
while (True):
    for event in pygame.event.get ():
       if event.type == pygame.QUIT:
            pygame.quit ()
    screen.fill ("white")
    c1.draw_circle ()
    pygame.display.update ()
