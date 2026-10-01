import pygame
pygame.init ()
W = 900
H = 500
background = pygame.image.load ("images/beach.jpg")
background = pygame.transform.scale (background,(900,500))
greenyim = pygame.image.load ("images/greeny.webp")
greenyim = pygame.transform.scale (greenyim, (50,50))
screen = pygame.display.set_mode ((W,H))
clock = pygame.time.Clock ()
class player (pygame.sprite.Sprite):
    def __init__ (self, x, y, velo):
        super (). __init__ ()
        self.x = x
        self.y = y
        self.velo = velo
        self.image = greenyim
        self.rect = self.image.get_rect (center =(self.x,self.y))
    def update (self):
        if self.rect.y < 500:
            self.rect.y += 0.5
        elif self.rect.y > 500:
            self.rect.y=500
greeny = player (200,200,0)
greenygroup = pygame.sprite.Group ()
greenygroup.add (greeny)
while (True):
    clock.tick (60)
    for event in pygame.event.get ():
       if event.type == pygame.QUIT:
            pygame.quit ()
    screen.blit (background,(0,0))
    greenygroup.update ()
    greenygroup.draw (screen)
    pygame.display.update ()