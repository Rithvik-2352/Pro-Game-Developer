import pygame
pygame.init ()
W = 2000
H = 1000
background = pygame.image.load ("images/Space 2.png")
background = pygame.transform.scale (background,(2000,1000))
redship = pygame.image.load ("images/red ship.png")
redship = pygame.transfrom.scale (redship, (400,200))
yellowship = pygame.image.load ("images/yellow ship.png")
yellowship = pygame.transfrom.scale (yellowship, (400,200))
screen = pygame.display.set_mode ((W,H))
class ship (pygame.sprite.Sprite):
    def __init__ (self,color,x,y):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        if self.color == "red":
            self.image = redship
            self.rect = self.image.get_rect ()
            self.rect.topleft = (self.x,self.y)
        elif self.color == "yellow":
            self.image = yellowship
            self.rect = self.image.get_rect ()
            self.rect.topleft = (self.x,self.y)
    def update (self, key):
        if self.color == "red":
            if key == [pygame.K_w]:
                self.y += 1
            if key == [pygame.K_s]:
                self.y -= 1
            if key == [pygame.K_a]:
                self.x -= 1
            if key == [pygame.K_d]:
                self.x += 1
        if self.color == "yellow":
            if key == [pygame.K_UP]:
                self.y += 1
            if key == [pygame.K_DOWN]:
                self.y -= 1
            if key == [pygame.K_LEFT]:
                self.x -= 1
            if key == [pygame.K_RIGHT]:
                self.x += 1
leftplayer = ship ("red",500,500)         
rightplayer = ship ("yellow",1500,500)                       
while (True):
    for event in pygame.event.get ():
       if event.type == pygame.QUIT:
            pygame.quit ()
    screen.blit (background,(0,0))
    pygame.display.update ()