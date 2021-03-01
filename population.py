import numpy as np
from pprint import pprint

class population :
    def __init__(self, screen) :
        self.pool=[]
        self.size=0
        self.screen=screen
        self.laxe=0

    def add(self,entity) :
        self.pool.append(entity)
        self.size+=1

    def reinit(self):
        for i in range(self.size):
            self.pool[i].snapshot(self.laxe)
    
    def differtiate(self) :
        for i in range(self.size):
            self.pool[i].update_weights(self.laxe)

    def are_all_dead(self) :
        for i in range(self.size):
            if self.pool[i].is_alive() :
                return False
        return True

    def get_best(self):
        ibest=0
        for i in range(1,self.size):
            if self.pool[ibest].score[self.laxe] < self.pool[i].score[self.laxe] :
                ibest=i
        
        return self.pool[ibest]

    def fall(self) :
        for i in range(self.size ):
            self.pool[i].fall()
    
    def take_decision(self,tx,tl,tu):
        for i in range(self.size):
            if self.pool[i].brain.decision(self.pool[i].rect.centery,tx,tl,tu) > 0 :
                self.pool[i].jump()

    def blit(self):
        for i in range(self.size):
            if self.pool[i].is_alive() :
                self.screen.blit(self.pool[i].surface, self.pool[i].rect)

    def update_score(self, tx) :
        if self.pool[0].rect.centerx ==tx :
            for i in range(self.size): 
                self.pool[i].score+=1

    def clone(self, entity):
        for i in range(self.size):
            self.pool[i].brain.weights=np.copy(entity.brain.weights)

    def check_deaths(self, t1, t2) :
        for i in range(self.size):
            if self.pool[i].rect.y> 600 or self.pool[i].rect.y<0 :
                self.pool[i].kill()
            elif self.pool[i].collide(t1) :
                self.pool[i].kill()
            elif self.pool[i].collide(t2) :
                self.pool[i].kill()

    def show_all(self):
        for i in range(self.size) :
            pprint(self.pool[i].brain.weights)

    def change_axe(self):
        self.laxe=(self.laxe+1)%4