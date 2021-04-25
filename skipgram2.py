import numpy as np
def initializeweight (self):
    self.emb_wei = np.random.uniform(-0.9,0.9, (self.voc, self.wordemb)) #first
    self.context_wei = np.random.uniform(-0.9, 0.9, (self.voc, self.wordemb)) #sec

def forw_pass(self, X): #first layer
    H = np.dot(self.emb_wei.T, X)
    U = np.dot(self.cont_wei.T, H)
    y_h = self.softmax(U)
    return y_h, H, U

def