from circleshape import *
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, WHITE_COLOR
import pygame
import random

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

    # Each time an asteroid is hit with a bullet, if it's not a small asteroid, it will split
    # into two asteroids. If a big asteroid is hit, it will split into two medium asteroids.
    # If a medium asteroid is hit, it will split into two small asteroids.
    # If a small asteroid is hit, the asteroid will disappear.
    def split(self):
        # Delete the current asteroid
        self.kill()

        # If the current radius of the asteroid is already the smallest asteroid, then return.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Get a new travel angle for the new asteroids.
        new_angle = random.uniform(20, 50)

        # Create new velocity angles for the two new asteroids.
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)

        # Compute the new radius of the two smaller asteroids about to be spawned.
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects at the current asteroid position with the new radius.
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)

        # Set the velocity of the new asteroids to the new vectors and make it move faster
        # by scaling it up by a multiple of 1.2
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2
