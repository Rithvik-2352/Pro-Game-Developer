import pygame
from shapes import Circle
pygame.init ()
W = 500
H = 500
screen = pygame.display.set_mode ((W,H))
c1 = Circle (250,250,50,15,10,"blue")
while (True):
    screen.fill ("white")
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.draw_circle ()
            pygame.display.update ()
        if event.type == pygame.MOUSEBUTTONUP:
            c1.circle_grow ()
            pygame.display.update ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                c1.circle_down ()
                pygame.display.update ()
            if event.key == pygame.K_UP:
                c1.circle_up ()
                pygame.display.update ()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            c1.x = pos [0]
            c1.y = pos [1]
            c1.draw_circle ()
            pygame.display.update ()
