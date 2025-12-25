from circleshape import *
from constants import *

class Shot(CircleShape):
    """
    In our game, bullets:

        Are small circles
        Move at a constant speed in a straight line
        Split up asteroids when they collide with them
        Are spawned by player input (spacebar) and move in the direction the player is facing
    """
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt