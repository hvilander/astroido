import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        x = self.position.x
        y = self.position.y
        pygame.draw.circle(screen, "white", (x,y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

