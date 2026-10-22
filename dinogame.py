import pygame
pygame.init ()
W = 2000
H = 1000
bird1 = pygame.image.load ("images/Assets/Bird/Bird1.png")
bird2 = pygame.image.load ("images/Assets/Bird/Bird2.png")
largecactus1 = pygame.image.load ("images/Assets/Cactus/LargeCactus1.png")
largecactus2 = pygame.image.load ("images/Assets/Cactus/LargeCactus2.png")
largecactus3 = pygame.image.load ("images/Assets/Cactus/LargeCactus3.png")
smallcactus1 = pygame.image.load ("images/Assets/Cactus/SmallCactus1.png")
smallcactus2 = pygame.image.load ("images/Assets/Cactus/SmallCactus2.png")
smallcactus3 = pygame.image.load ("images/Assets/Cactus/SmallCactus3.png")
dinodead = pygame.image.load ("images/Assets/Dino/DinoDead.png")
dinoduck1 = pygame.image.load ("images/Assets/Dino/DinoDuck1.png")
dinoduck2 = pygame.image.load ("images/Assets/Dino/DinoDuck2.png")
dinojump = pygame.image.load ("images/Assets/Dino/DinoJump.png")
dinorun1 = pygame.image.load ("images/Assets/Dino/DinoRun1.png")
dinorun2 = pygame.image.load ("images/Assets/Dino/DinoRun2.png")
dinostart = pygame.image.load ("images/Assets/Dino/DinoStart.png")
cloud = pygame.image.load ("images/Assets/Other/Cloud.png")
gameover = pygame.image.load ("images/Assets/Other/GameOver.png")
reset = pygame.image.load ("images/Assets/Other/Reset.png")
track = pygame.image.load ("images/Assets/Other/Track.png")
track = pygame.transform.scale (track, (4000,24))
screen = pygame.display.set_mode ((W,H))
game = True
track_x = 2000
track_y = 950
class dino (pygame.Sprite.sprite):
    def __init__ (self, x, y):
        super (). __init__ ()
        self.x = x
        self.y = y
        self.run_images = [dinorun1, dinorun2]
        self.duck_images = [dinoduck1, dinoduck2]
        self.isjumping = False
        self.isducking = False
        self.image = self.run_images [0]
        self.rect = self.image.get_rect ()
        self.rect.x = self.x
        self.rect.bottom = track_y
while (True):
    for event in pygame.event.get ():
       if event.type == pygame.QUIT:
            pygame.quit ()
    screen.fill ("white")
    screen.blit (track, (track_x, track_y))
    if game == True:
        if abs (track_x) > 400:
            track_x = 0
        track_x -= 0.5
    pygame.display.update ()