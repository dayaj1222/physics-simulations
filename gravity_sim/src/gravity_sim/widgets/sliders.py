from typing import Tuple

import pygame


class Slider:
    def __init__(
        self,
        value: float = 5,
        min: float = 0,
        max: float = 10,
        name: str = "Slider",
        position: Tuple[int, int] = (0, 0),
        width: int = 20,
        height: int = 5,
    ) -> None:
        # Value
        self.value = value
        self.min = min
        self.max = max
        self.name = name

        self.position = position
        self.width = width
        self.height = height

        # State
        normalized = (value - min) / (max - min) if max != min else 0
        self.knob_x = position[0] + normalized * width
        self.is_dragging = False
        self.bar_rect = pygame.Rect(self.position, (self.width, self.height))

        # Color
        self.bar_color = "Grey"
        self.knob_color = "Blue"
        self.border_color = "Green"
        self.text_color = "White"

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(
            surface,
            self.bar_color,
            pygame.Rect(self.position, (self.width, self.height)),
        )
        knob_center = (int(self.knob_x), int(self.position[1] + self.height / 2))
        pygame.draw.circle(surface, self.knob_color, knob_center, self.height)

        # Text
        font = pygame.font.Font(None, 24)
        label_y = self.position[1] - 8
        value_y = self.position[1] - 20

        min_surf = font.render(str(self.min), True, self.text_color)
        surface.blit(min_surf, min_surf.get_rect(center=(self.position[0], label_y)))

        max_surf = font.render(str(self.max), True, self.text_color)
        surface.blit(
            max_surf, max_surf.get_rect(center=(self.position[0] + self.width, label_y))
        )

        value_surf = font.render(f"{self.value:.2f}", True, self.text_color)
        surface.blit(
            value_surf, value_surf.get_rect(center=(int(self.knob_x), value_y))
        )

        name_surface = font.render(f"{self.name}", True, self.text_color)
        surface.blit(
            name_surface,
            name_surface.get_rect(
                center=(
                    int(self.position[0] + self.width / 2),
                    int(self.position[1] + 20),
                )
            ),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.bar_rect.collidepoint(event.pos):
                self.is_dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_dragging = False

        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            self.knob_x = max(
                self.position[0], min(event.pos[0], self.position[0] + self.width)
            )
            normalized = (self.knob_x - self.position[0]) / self.width
            self.value = self.min + normalized * (self.max - self.min)
