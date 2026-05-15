import random

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event




class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.min_radius = ASTEROID_MIN_RADIUS


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > self.min_radius:
            log_event("asteroid_split")
            new_radius = self.radius - self.min_radius
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            random_angle = random.uniform(20, 50)
            new_asteroid1.velocity = pygame.Vector2(1, 0).rotate(random_angle) * random.uniform(50, 150)
            new_asteroid2.velocity = pygame.Vector2(1, 0).rotate(-random_angle) * random.uniform(50, 150)

            return [new_asteroid1, new_asteroid2]
        else:
            return []