import pygame
from constants import LINE_WIDTH, SHOT_LIFETIME_SECONDS, SHOT_RADIUS, SHOT_SPEED


class Shot(pygame.sprite.Sprite):
    #def __init__(self, position, velocity):
    def __init__(self, x, y, velocity):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.radius = SHOT_RADIUS
        self.lifetime = SHOT_LIFETIME_SECONDS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()