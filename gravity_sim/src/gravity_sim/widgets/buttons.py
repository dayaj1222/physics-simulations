from typing import Tuple

import pygame
import pymunk

from gravity_sim import bodies


class Button:
    def __init__(self, name: str, pos: Tuple[int, int]) -> None:
        self.name = name
        self.pos = pos
        self.button_rect = pygame.Rect(pos, (100, 60))
        self.color = (0, 128, 255)
        self.text_color = (255, 255, 255)

    def draw(self, surface: pygame.Surface) -> None:
        font = pygame.font.SysFont(None, 36)

        pygame.draw.rect(surface, self.color, self.button_rect)

        text_surface = font.render(self.name, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        surface.blit(text_surface, text_rect)

    def handle_click(
        self,
        event: pygame.event.Event,
        bodies: list[bodies.Body],
        space: pymunk.Space,
        sprites: pygame.sprite.Group,
    ) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and self.button_rect.collidepoint(
            event.pos
        ):
            for body in bodies:
                space.remove(body.physics_body, body.shape)
                sprites.remove(body)
            bodies.clear()
