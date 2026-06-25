import pygame
pygame.init ()
W = 500
H = 500
screen = pygame.display.set_mode ((W,H))
class Rectangle ():
    def __init__ (self, x, y, h, w, color):
       self.x = x
       self.y = y
       self.h = h
       self.w = w
       self.color = color
    def draw_rect(self):
       pygame.draw.rect (screen,self.color,(self.x, self.y, self.w, self.h))
class Circle ():
    def __init__  (self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def draw_circle(self):
        pygame.draw.circle (screen,self.color,(self.x,self.y),self.r)
# r1=Rectangle (50,50,100,150,"black")
# c1=Circle (250,250,50,"blue")
# while (True):
#     for event in pygame.event.get ():
#        if event.type == pygame.QUIT:
#             pygame.quit ()
#     screen.fill ("white")
#     r1.draw_rect ()
#     c1.draw_circle ()
#     pygame.display.update ()
