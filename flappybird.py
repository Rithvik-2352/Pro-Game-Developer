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
ground_x = 0
game = False
images = [birdflapmid, birdflapup, birdflapmid, birdflapdown]
clock = pygame.time.Clock ()
flying = True
class bird (pygame.sprite.Sprite):
    def __init__ (self, x, y, velo):
        super (). __init__ ()
        self.x = x
        self.y = y
        self.velo = velo
        self.counter = 0
        self.index = 0
        self.clicked = False
        self.image = images [self.index]
        self.rect = self.image.get_rect ()
        self.rect.topleft = (self.x, self.y)
    def update (self):
        global game
        if flying == False:
            self.velo += 0.01
            if self.velo > 5:
                self.velo = 5
            if self.rect.y  < 570:
                self.rect.y += self.velo
                
        if game == True:
            if pygame.mouse.get_pressed ()[0] and self.clicked == False:
                print ("mouse pressed")
                self.clicked = True
                self.velo = -1.5
            if not pygame.mouse.get_pressed ()[0]:
                self.clicked = False
            self.counter += 1
            if self.counter >= 100:
                self.counter = 0
                if self.index < 3:
                    self.index +=1
                else:
                    self.index = 0
                old_center = self.rect.center
                self.image = images [self.index]
                self.rect = self.image.get_rect ()
                self.rect.center = old_center
flappy = bird (332,384,5)
flappygroup = pygame.sprite.Group ()
flappygroup.add (flappy)
while (True):
    clock.tick (180)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == True:
            game = True
            flying = False
    if game == True:
        flappygroup.update ()
        if ground_x >= -432:
            ground_x -= 0.5
        else:
            ground_x = 0
    if flappy.rect.y >= 570:
        game = False
    print (flappy.rect.y)
    screen.blit (background,(0,0))
    screen.blit (ground, (ground_x,600))
    flappygroup.draw (screen)
    pygame.display.update ()
