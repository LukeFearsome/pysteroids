from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20,50)

        splitAsteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        splitAsteroid1.velocity = (self.velocity*1.2).rotate(split_angle)

        splitAsteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        splitAsteroid2.velocity = (self.velocity*1.2).rotate(-split_angle)
 


    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt