import pygame
import math
from checkpoint import Checkpoint
from checkpoint import getCheckpoint
from obstacle import Obstacle
from obstacle import getObstacle



GOALREWARD = 1
LIFE_REWARD = 0
PENALTY = -1



def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

def distance(pt1, pt2):
    return(((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)**0.5)


class myPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class AbstractBoat:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    



class DroneBoat(AbstractBoat):
    IMG = pygame.image.load("boat.png")
    START_POS = (180, 200)



    def action(self, choice):
        if choice == 0:
            self.reduce_speed()
        elif choice == 1:
            self.move_forward()
        elif choice == 2:
            self.rotate(right=True)
            
        elif choice == 3:
            self.rotate(left=True)
        
        pass
    
 
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)


    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def reset(self):

        self.x, self.y = self.START_POS
        self.vel = 0
        self.angle = 0
        self.acceleration = 0.1

    def cast(self,checkpoints,obstacles):
        observations=[]
        for checkpoint in checkpoints:
            d1=distance(myPoint(checkpoint.x,checkpoint.y),myPoint(self.x,self.y))
            observations.append(d1)

        for obstacle in obstacles:
            d2=distance(myPoint(obstacle.x,obstacle.y),myPoint(self.x,self.y))
            observations.append(d2)

        return observations








class RacingEnv:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)

        self.fps = 10
        self.width = 1400
        self.height = 600
        self.history = []

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("BOAT DQN")
        self.screen.fill((0,0,0))
        self.back_image = pygame.image.load("boat.png").convert()
        self.back_rect = self.back_image.get_rect().move(0, 0)
        self.action_space = None
        self.observation_space = None
        self.game_reward = 0
        self.score = 0
 
        self.reset()


    def reset(self):
        self.screen.fill((0, 0, 0))

        self.boat = DroneBoat(180, 200)
        self.checkpoints = getCheckpoint()
        self.obstacles = getObstacle()
        self.game_reward = 0

    def step(self, action):

        done = False
        self.boat.action(action)
        reward = LIFE_REWARD

        # Check if car passes Goal and scores
        
        for checkpoint in self.checkpoints:
            
            if checkpoint.isactiv:

                reward += GOALREWARD

        for obstacle in self.obstacles:
            if distance(myPoint(self.boat.x,self.boat.y),myPoint(obstacle.x,obstacle.y))<52:
                obstacle.iscollid=True
                reward += PENALTY
                done = True

        #check if car crashed in the wall
        
        new_state = self.boat.cast(self.obstacles,self.checkpoints)
        #normalize states
        if done:
            new_state = None

        return new_state, reward, done

    def render(self, action):

        pygame.time.delay(10)
        self.clock = pygame.time.Clock()
        self.screen.fill((104, 170, 242))
        self.boat.draw(self.screen)
        
        for checkpoint in self.checkpoints:
            if distance(myPoint(self.boat.x,self.boat.y),myPoint(checkpoint.x,checkpoint.y))<102:
                checkpoint.isactiv=True
            checkpoint.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
            if distance(myPoint(self.boat.x,self.boat.y),myPoint(obstacle.x,obstacle.y))<52:
                obstacle.iscollid=True
                    
            else:
                obstacle.iscollid=False     
            
        self.clock.tick(self.fps)
        pygame.display.update()
    def close(self):
        pygame.quit()

