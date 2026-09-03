import pygame
pygame.init ()
W = 2000
H = 1000
background = pygame.image.load ("images/Space 2.png")
background = pygame.transform.scale (background,(2000,1000))
redship = pygame.image.load ("images/red ship.png")
redship = pygame.transform.scale (redship, (250,206.5))
yellowship = pygame.image.load ("images/yellow ship.png")
yellowship = pygame.transform.scale (yellowship, (250,206.5))
redship = pygame.transform.rotate (redship,90)
yellowship = pygame.transform.rotate (yellowship,270)
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
    def move (self, key):
        if self.color == "red":
            if key  [pygame.K_w]:
                if self.rect.y >= 0:
                    self.rect.y -= 1
            if key  [pygame.K_s]:
                if self.rect.y <= 760:
                    self.rect.y += 1
            if key  [pygame.K_a]:
                if self.rect.x >= 0:
                    self.rect.x -= 1
            if key  [pygame.K_d]:
                if self.rect.x <= 790:
                    self.rect.x += 1
        if self.color == "yellow":
            if key  [pygame.K_UP]:
                if self.rect.y >= 0:
                    self.rect.y -= 1
            if key  [pygame.K_DOWN]:
                if self.rect.y <= 760:
                    self.rect.y += 1
            if key  [pygame.K_LEFT]:
                if self.rect.x >= 1005:
                    self.rect.x -= 1
            if key  [pygame.K_RIGHT]:
                if self.rect.x <= 1790:
                    self.rect.x += 1
class bullet (pygame.sprite.Sprite):
    def __init__ (self,color,x,y):
        super (). __init__ ()
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect (self.x,self.y, 10, 3)
    def update (self):
        if self.color == "red":
            if self.x >= 2000:
                self.kill ()
            self.x += 1
        if self.color == "yellow":
            if self.x <= 0:
                self.kill ()
            self.x -= 1
leftplayer = ship ("red",500,500)         
rightplayer = ship ("yellow",1500,500)  
leftshipgroup = pygame.sprite.Group ()     
rightshipgroup = pygame.sprite.Group ()     
leftshipgroup.add (leftplayer)  
rightshipgroup.add (rightplayer)   
mid_border = pygame.Rect (1000,0,5,1000)     
redbulletgroup = pygame.sprite.Group () 
yellowbulletgroup = pygame.sprite.Group ()
while (True):
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                redbullet = bullet ("red",leftplayer.x,leftplayer.y)
                redbulletgroup.add (redbullet)
            if event.key == pygame.K_RSHIFT:
                yellowbullet = bullet ("yellow",rightplayer.x,rightplayer.y)
                yellowbulletgroup.add (yellowbullet)
        
    screen.blit (background,(0,0))
    pygame.draw.rect (screen,"red",mid_border)
    for redbullet in redbulletgroup:
        pygame.draw.rect (screen,"red",redbullet.rect)
    redbulletgroup.update ()
    for yellowbullet in yellowbulletgroup:
        pygame.draw.rect (screen, "yellow", yellowbullet.rect)
    yellowbulletgroup.update ()
    key = pygame.key.get_pressed ()
    leftplayer.move (key)
    rightplayer.move (key)
    leftshipgroup.draw (screen)
    rightshipgroup.draw (screen)
    pygame.display.update ()