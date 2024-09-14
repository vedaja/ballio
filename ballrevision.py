import pygame
from pygame.locals import *
import random

pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Ball")

balls=[]

class BallGame:
    def __init__(self):
        self.x=random.randint(0,600)
        self.y=random.randint(0,600)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.size=random.randint(0,50)

    def draw(self):
        self.rect=pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

for i in range(1,31,1):
    balls.append(BallGame())

b1=BallGame()
b1.x=300
b1.y=300
b1.size=15

while True:
    screen.fill((0,0,0))

    for y in balls:
        y.draw()

    b1.draw()

    for x in balls:
        if b1.rect.colliderect(x.rect):
            if b1.size>=x.size:
                b1.size=b1.size+5
                balls.remove(x)
                break
            else:
                print("game over")

    for event in pygame.event.get():
        if event.type==MOUSEMOTION:
            b1.x=event.pos[0]
            b1.y=event.pos[1]

        if event.type==QUIT:
            pygame.quit()
            exit()


    pygame.display.update()


















