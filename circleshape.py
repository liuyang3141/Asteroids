import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass
    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, circle1, circle2):
        distance = circle1.radius + circle2.radius

        return circle1.position.distance_to(circle2.position) <= distance
