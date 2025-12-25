from circleshape import *
from constants import *
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        # (the surface to draw on, the color, its center position, radius, the width of the line)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Otherwise we need to spawn 2 new asteroids:
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_ast_vector1 = self.velocity.rotate(new_angle)
        new_ast_vector2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_new1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_new2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_new1.velocity = new_ast_vector1 * 1.2
        asteroid_new2.velocity = new_ast_vector2 * 1.2