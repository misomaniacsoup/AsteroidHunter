from circleshape import CircleShape
import pygame
from logger import log_event
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, color="white", center=self.position, radius=self.radius)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            random.uniform(20, 50)
            new_vector = self.velocity.rotate(random.uniform(20, 50))
            new_vector2 = self.velocity.rotate(random.uniform(-20, -50))
            self.velocity.rotate(random.uniform(-20, -50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_vector * 1.2
            new_asteroid2.velocity = new_vector2 * 1.2