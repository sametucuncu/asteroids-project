from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        # (the surface to draw on, the color, its center position, radius, the width of the line)
        
    def update(self, dt):
        self.position += self.velocity * dt