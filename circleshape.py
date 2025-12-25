# In Pygame, there's a base Sprite class that represents visual objects.
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
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    # Everything that collides will inherit from this Class, so this is a good place to add collision logic.
    def collides_with(self, other):
        # Get the distance between the two shapes
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius