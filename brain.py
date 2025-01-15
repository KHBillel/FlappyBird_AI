import numpy as np

class brain :
    def __init__(self, old_brain=None):
        if old_brain :
            self.weights = old_brain.weights
        else :
            self.weights = np.random.uniform(-1,1,size=(4,1))


    def decision(self,by,tx,tl,tu):
        return np.tanh(np.matmul(np.array([[by,tx,tl,tu]]), self.weights))
