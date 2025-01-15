import pygame
from tube_maker import tube_maker
from bird_maker import bird_maker
from population import population
from pprint import pprint
import time
import numpy as np

BLACK = (0, 0, 0)
RED = (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode((800, 600))
best = None 
pop=population(screen)
iteration=0

while True :
    if best == None :
        for i in range(1):
            pop.add(bird_maker.genBird(600))
    else :
        pop.reinit()
        pop.clone(best)
        pprint(best.grad)
    
    pop.differtiate()
    # trained weights : pop.pool[0].brain.weights=np.array([[ 3.58840662],[ -0.48806278],[-0.65371758],[-5.71694412]])
    pop.pool[0].brain.weights=np.array([[ 3.58840662],[ -0.48806278],[-0.65371758],[-5.71694412]])
    tube1, tube2=tube_maker.genTubes(800,600)
    while not pop.are_all_dead():
        # Clearing all sprites and rebuilding the screen:
        screen.fill(BLACK)


        pop.take_decision(tube1.rect.centerx,tube2.rect.centery,tube1.rect.centery)
        pop.fall()
        tube1.move()
        tube2.move()
        #pop.update_score(tube1.rect.centerx)
        pop.check_deaths(tube1, tube2)

        if tube1.rect.right<=0 :
            del tube1, tube2
            tube1, tube2= tube_maker.genTubes(800,600)

        pop.blit()
        screen.blit(tube1.surface, tube1.rect)
        screen.blit(tube2.surface, tube2.rect)
        pygame.display.flip()
        pprint(pop.get_best().brain.weights)
        time.sleep(1/30)

    del tube1, tube2
    #pop.show_all()
    best=pop.get_best()
    pop.change_axe()
    pygame.display.set_caption("Generation : "+str(iteration)+"     Score:"+str(best.score)) 
    iteration+=1
