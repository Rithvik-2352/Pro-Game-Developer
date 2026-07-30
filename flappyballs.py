import pygame
from shapes import Rectangle
from shapes import Circle
pygame.init ()
W = 500
H = 500
screen = pygame.display.set_mode ((W,H))
c1=Circle (250,100,10,100,0,"blue")
c2=Circle (300,100,20,200,0,"green")
clock = pygame.time.Clock ()
while (True):
    dt = clock.tick (60)/1000
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                c1.y = c1.y - 50
    screen.fill ("white")
    c1.update_gravity (dt)
    c1.draw_circle ()
    c2.update_gravity (dt)
    c2.draw_circle ()
    print (c1.x)
    pygame.display.update ()
