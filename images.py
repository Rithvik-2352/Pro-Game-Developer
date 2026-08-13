import pygame
import time
pygame.init ()
W = 1000
H = 500
screen = pygame.display.set_mode ((W,H))
background = pygame.image.load ("images/beach.jpg")
background = pygame.transform.scale (background,(1000,500))
bird = pygame.image.load ("images/bird.png")
bird = pygame.transform.scale (bird,(50,50))
class character (pygame.sprite.Sprite):
    def __init__ (self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = bird
        self.rect = self.image.get_rect ()
        self.rect.topleft = (self.x,self.y)
    def update (self, key):
        if key [pygame.K_UP]:
            self.rect.y -= 1
        if key [pygame.K_DOWN]:
            self.rect.y += 1  
        print (self.rect.y)
bird1 = character (500,250)
birdGroup = pygame.sprite.Group () 
birdGroup.add (bird1)
clock = pygame.time.Clock ()       
while (True):
    clock.tick(60)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bird1.rect.x += 10
            if event.key == pygame.K_LEFT:
                bird1.rect.x -= 10
            if event.key == pygame.K_SPACE:
                bird1.rect.y -= 40
                

    screen.blit (background,(0,0))
    bird1.rect.y +=0.5
    key = pygame.key.get_pressed ()
    birdGroup.update (key)
    birdGroup.draw (screen)
    pygame.display.update ()
