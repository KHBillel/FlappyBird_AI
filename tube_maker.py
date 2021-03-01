import random
import pygame

GREEN = (0,255,0)

class tube :
    def __init__(self,x,y,h) :
        self.x=x
        self.y=y
        self.w=30
        self.h=h

        self.surface = pygame.Surface((30, h))
        self.surface.fill(GREEN)
        self.rect = self.surface.get_rect()
        self.rect.midbottom = (x, y)

    def move(self) :
        self.rect.centerx-=15

class tube_maker_ :
    def genTubes(self,w,h):
        t=random.randrange(0,500)
        tube1=tube(w,t,t)
        tube2=tube(w,600,h-100-t)
        return tube1, tube2

tube_maker=tube_maker_()