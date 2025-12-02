import pygame
from pygame.math import Vector2


class Body(pygame.sprite.Sprite):
    def __init__(
        self,
        mass: float,
        radius: float,
        position: Vector2,
        velocity: Vector2,
        image_path: str,
    ) -> None:
        super().__init__()
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, (radius * 2, radius * 2))
        self.rect = self.image.get_rect(center=(position.x, position.y))

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)
