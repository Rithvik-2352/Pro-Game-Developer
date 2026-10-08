import pygame
import random
import time
pygame.init ()
W = 864
H = 768
screen = pygame.display.set_mode ((W,H))
background = pygame.image.load ("images/flappybackground.png")
pipeim = pygame.image.load ("images/Pipe.png")
restart = pygame.image.load ("images/Restart.png")
birdflapup = pygame.image.load ("images/birdflapu.png")
birdflapmid = pygame.image.load ("images/birdflapm.png")
birdflapdown = pygame.image.load ("images/birdflapd.png")
gameover = pygame.image.load ("images/268-2680778_flappy-bird-game-over-png-transparent-png.png")
gameover = pygame.transform.scale (gameover,(300,90))
restart = pygame.image.load ("images/Restart.png")
ground = pygame.image.load ("images/flappyground.png")
ground = pygame.transform.scale (ground,(1800,168))
ground_x = 0
game = False
images = [birdflapmid, birdflapup, birdflapmid, birdflapdown]
clock = pygame.time.Clock ()
flying = True
score = 0
font = pygame.font.SysFont ("Bauhaus 93", 40)
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
            self.velo += 0.02
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
class pipe (pygame.sprite.Sprite):
    def __init__ (self, x, y, direction, velo):
        super (). __init__ ()
        self.x = x
        self.y = y
        self.direction = direction
        self.velo = velo
        self.image = pipeim
        self.rect = self.image.get_rect ()
        if self.direction == "top":
            self.image = pygame.transform.flip (self.image, False, True)
            self.rect.bottomleft = (self.x, self.y - 80)
        if self.direction == "bottom":
                    self.rect.topleft = (self.x, self.y + 80)
    def update (self):
        self.rect.x -= self.velo
        if self.rect.x <= -10:
            self.kill ()
flappy = bird (50,384,5)
flappygroup = pygame.sprite.Group ()
flappygroup.add (flappy)
pipegroup = pygame.sprite.Group ()
pipe_frequency = 2000
last_pipe = pygame.time.get_ticks() - pipe_frequency
screen.blit (background,(0,0))
screen.blit (ground, (ground_x,600))
while (True):
    clock.tick (220)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == True:
            game = True
            flying = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos ()
            print (pos)
            if game == False:
                if 410 <= pos [0] <= 530 and 200 <= pos [1] <= 342:
                    game = True
                    flappy.rect.x = 50
                    flappy.rect.y = 384
                    pipegroup.empty ()
                    score = 0
    if pygame.sprite.groupcollide (flappygroup,pipegroup,False, False):
        game = False
        if game == False:
            flying = True
            if flappy.rect.y >= 570:
                flappy.rect.y -= 0.1
            else:
                flappy.rect.y = 570
            screen.blit (gameover, (400,100))
            screen.blit (restart, (410,200))
    if game == True:
        for p in pipegroup:
            if p.rect.left < flappy.rect.left:
                score += 0.5
                p.kill ()
        flappygroup.update ()
        if ground_x >= -432:
            ground_x -= 0.5
        else:
            ground_x = 0
        time_now = pygame.time.get_ticks ()
        if time_now - last_pipe >= pipe_frequency:
            height = random.randint (-100, 100)
            bottom_pipe = pipe (W, H/2 + height, "bottom", 2)
            top_pipe = pipe (W, H/2 + height, "top", 2)
            pipegroup.add (bottom_pipe)
            pipegroup.add (top_pipe)
            last_pipe = time_now
        pipegroup.update ()
        screen.blit (background,(0,0))
        text = font.render (str(round(score,1)),True, "white")
        screen.blit (text, (430,50))
        screen.blit (ground, (ground_x,600))
        flappygroup.draw (screen)
        pipegroup.draw (screen)
    if flappy.rect.y >= 570:
        game = False
    pygame.display.flip ()
