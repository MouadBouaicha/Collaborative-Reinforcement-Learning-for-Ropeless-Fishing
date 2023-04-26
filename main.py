import pygame
import time
import math
import checkpoint
import obstacle

Reward=0
class myPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def distance(pt1, pt2):
    return(((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)**0.5)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)


RED_CAR = pygame.image.load("boat.png")



WIN = pygame.display.set_mode((1400, 600))
pygame.display.set_caption("Racing Game!")

FPS = 60

checkpoints = checkpoint.getCheckpoint()
obstacles=obstacle.getObstacle()
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
        

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

    def collision(self, obstacle):
         if distance(myPoint(player_car.x,player_car.y),myPoint(obstacle.x,obstacle.y))<20:        
            return True
         return False



class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)


def draw(win, player_car):
    
    win.fill((104, 170, 242))
    player_car.draw(win)
    
    for checkpoint in checkpoints:
            if distance(myPoint(player_car.x,player_car.y),myPoint(checkpoint.x,checkpoint.y))<102:
                checkpoint.isactiv=True
            checkpoint.draw(WIN)

    for obstacle in obstacles:
            if distance(myPoint(player_car.x,player_car.y),myPoint(obstacle.x,obstacle.y))<52:
                obstacle.iscollid=True
                print("collision")
            else:
                obstacle.iscollid=False     
            obstacle.draw(WIN)
    
    pygame.display.update()


run = True
clock = pygame.time.Clock()

player_car = PlayerCar(4, 4)

while run:
    clock.tick(FPS)

    draw(WIN,  player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT] :
        player_car.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player_car.rotate(right=True)
    if keys[pygame.K_UP]  :
    
        moved = True
        player_car.move_forward()
    if not moved:
        player_car.reduce_speed()
    
            

    


pygame.quit()