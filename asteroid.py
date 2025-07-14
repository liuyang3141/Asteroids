from circleshape import *
from constants import WHITE_COLOR
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override the draw() method to draw the asteroid as a pygame.draw.circle().
    # Use its position, raidus, and a width of 2
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, 2)

    # Override the update() method so that it moves in a straight line at constant speed.
    # On each frame, it should add (self.velocity * dt) to its position (get self.velocity
    # from its parent class, CircleShape)
    def update(self, dt):
        self.position += self.velocity * dt
