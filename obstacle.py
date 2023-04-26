import pygame

class Obstacle():
    def __init__(self, x, y):
        self.x = x
        self.y= y
        self.iscollid = False

        
    
    def draw(self, win):
        pygame.draw.rect(win, (0,0,255), (self.x, self.y, 25, 25))



def getObstacle():
    Obstacles = []
    
    Obstacle1 = Obstacle(100,500)
    Obstacle2 = Obstacle(800,100)
    Obstacle3 = Obstacle(190,500)
    Obstacle4 = Obstacle(600,270)
    Obstacle5 = Obstacle(250,100)
    Obstacle6 = Obstacle(400,500)

    
    Obstacles.append(Obstacle1)
    Obstacles.append(Obstacle2)
    Obstacles.append(Obstacle3)
    Obstacles.append(Obstacle4)
    Obstacles.append(Obstacle5)
    Obstacles.append(Obstacle6)


    

    return(Obstacles)

