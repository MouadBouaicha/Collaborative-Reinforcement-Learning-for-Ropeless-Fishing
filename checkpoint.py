import pygame

class Checkpoint():
    def __init__(self, x, y):
        self.x = x
        self.y= y
        

        self.isactiv = False
    
    def draw(self, win):
        pygame.draw.circle(win,(255,0,0),(self.x,self.y),5)
        if self.isactiv:
            pygame.draw.circle(win, (0,255,0), (self.x,self.y), 5)
    
    

def getCheckpoint():
    checkpoints = []
    
    checkpoint1 = Checkpoint(1200,500)
    checkpoint2 = Checkpoint(1250,120)
    checkpoint3 = Checkpoint(190,200)
    checkpoint4 = Checkpoint(1030,270)
    checkpoint5 = Checkpoint(250,475)
    checkpoint6 = Checkpoint(650,500)

    
    checkpoints.append(checkpoint1)
    checkpoints.append(checkpoint2)
    checkpoints.append(checkpoint3)
    checkpoints.append(checkpoint4)
    checkpoints.append(checkpoint5)
    checkpoints.append(checkpoint6)


    

    return(checkpoints)

