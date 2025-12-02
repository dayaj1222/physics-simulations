import pygame
import pymunk


class Body(pygame.sprite.Sprite):
    def __init__(
        self,
        pymunk_body: pymunk.Body,
        position: pymunk.Vec2d,
        mass: float,
        radius: float,
        roughness: float,
        elasticity: float,
    ) -> None:
        super().__init__()
        self.mass = mass
        self.radius = radius
        self.roughness = roughness
        self.elasticity = elasticity

        # Position
        self.position = position
        self.physics_body = pymunk_body

        # Pymunk shape
        self.shape = pymunk.Circle(pymunk_body, radius)
        self.shape.elasticity = elasticity
        self.shape.friction = roughness

        # Images
        self.image = self._create_image()
        self.rect = self.image.get_rect(center=(int(position.x), int(position.y)))

    def _create_image(self) -> pygame.Surface:
        diameter = self.radius * 2
        image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(image, "Brown", (self.radius, self.radius), self.radius)
        return image

    def update(self):
        self.position = self.physics_body.position
        self.rect.center = (int(self.position.x), int(self.position.y))
