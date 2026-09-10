import pygame
pygame.init ()
W = 864
H = 768
screen = pygame.display.set_mode ((W,H))
background = pygame.image.load ("images/flappybackground.png")
pipe = pygame.image.load ("images/Pipe.png")
restart = pygame.image.load ("images/Restart.png")
birdflapup = pygame.image.load ("images/birdflapu.png")
birdflapmid = pygame.image.load ("images/birdflapm.png")
birdflapdown = pygame.image.load ("images/birdflapd.png")
ground = pygame.image.load ("images/flappyground.png")
ground = pygame.transform.scale (ground,(1800,168))
while (True):
    for event in pygame.event.get ():
       if event.type == pygame.QUIT:
            pygame.quit ()
    screen.blit (background,(0,0))
    screen.blit (ground, (0,600))
    pygame.display.update ()
