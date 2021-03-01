import pygame
import numpy as np
from brain import brain

YELLOW   = (255, 255, 0)

class bird :
    def __init__(self,h,old_gen=None) :
        self.h=h
        self.x=100
        self.y=int(h/2)
        self.alive=True
        self.score=[0,0,0,0]
        self.oscore=[0,0,0,0]
        self.grad=[0,0,0,0]
        self.laxe=0

        self.surface = pygame.Surface((20, 20))
        self.surface.fill(YELLOW)
        self.rect = self.surface.get_rect()
        self.rect.center= (self.x, self.y)
        self.brain=brain(old_gen)

    def snapshot(self,laxe):
        self.alive=True
        self.grad[laxe]=self.score[laxe]-self.oscore[laxe]
        self.oscore[laxe]=self.score[laxe]
        self.score[laxe]=0
        self.rect.centery=(self.h/2)
        self.laxe=(self.laxe+1)%4
        

    def update_weights(self,laxe) :
        bias=np.random.uniform(-5,5)
        self.brain.weights[laxe][0]+=(bias)

    def is_alive(self) :
        return self.alive
    
    def kill(self) :
        self.alive=False

    def get_score(self):
        return self.score[self.laxe]

    def jump(self) :
        self.rect.centery-=20
    
    def fall(self) :
        self.rect.centery+=10
        if self.is_alive() :
            self.score[self.laxe]+=1

    def collide(self, other) :
        if self.rect.colliderect(other) != 0:
            return True
        return False

class bird_maker_ :
    def genBird(self,h):
        return bird(h)

bird_maker = bird_maker_()
        



    