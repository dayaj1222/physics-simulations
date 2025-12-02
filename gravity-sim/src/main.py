from typing import Tuple

import pygame
import pymunk

from gravity_sim import bodies, physics
from gravity_sim.widgets import sliders
from gravity_sim.widgets.buttons import Button

# Constants
WIDTH = 1200
HEIGHT = 800
FPS = 120

GRAVITY = (0, 100)
MASS = 2
RADIUS = 8
ROUGHNESS = 0
ELASTICITY = 1
ELASTICITY_FLOOR = 1

pygame.init()
pygame.display.set_caption("Gravity Sim")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Layout
PANEL_WIDTH = 200
GROUND_HEIGHT = 50
side_panel = pygame.Surface((PANEL_WIDTH, HEIGHT))
main_area = pygame.Surface((WIDTH - PANEL_WIDTH, HEIGHT))

# State
RUNNING = True

# Bodies
bodies_list = []
sprites = pygame.sprite.Group()

# Physics engine
physic = physics.Physics(gravity=GRAVITY, bodies=bodies_list)


def add_object(
    pos: Tuple[float, float],
    mass: float = MASS,
    radius: float = RADIUS,
    roughness: float = ROUGHNESS,
    elasticity: float = ELASTICITY,
) -> None:
    moment = pymunk.moment_for_circle(mass, inner_radius=0, outer_radius=radius)
    pymunk_body = pymunk.Body(mass, moment)
    pymunk_body.position = pymunk.Vec2d(pos[0], pos[1])

    body = bodies.Body(
        pymunk_body, pymunk.Vec2d(pos[0], pos[1]), mass, radius, roughness, elasticity
    )

    bodies_list.append(body)
    physic.space.add(pymunk_body, body.shape)
    sprites.add(body)


def create_boundaries() -> None:

    main_width = WIDTH - PANEL_WIDTH

    static_body = pymunk.Body(body_type=pymunk.Body.STATIC)

    floor = pymunk.Segment(
        static_body,
        (0, HEIGHT - GROUND_HEIGHT),
        (main_width, HEIGHT - GROUND_HEIGHT),
        5,
    )
    wall_l = pymunk.Segment(static_body, (0, 0), (0, HEIGHT - GROUND_HEIGHT), 5)
    wall_r = pymunk.Segment(
        static_body, (main_width, 0), (main_width, HEIGHT - GROUND_HEIGHT), 5
    )
    ceiling = pymunk.Segment(static_body, (0, 0), (main_width, 0), 5)

    for segment in (floor, wall_l, wall_r, ceiling):
        segment.friction = ROUGHNESS
        segment.elasticity = ELASTICITY_FLOOR

    physic.space.add(static_body, floor, wall_l, wall_r, ceiling)


create_boundaries()

# Sliders
elasticity_slider = sliders.Slider(
    value=ELASTICITY,
    min=0,
    max=2,
    name="Elasticity",
    position=(10, 50),
    width=180,
    height=6,
)

mass_slider = sliders.Slider(
    value=MASS,
    min=0.1,
    max=10,
    name="Mass",
    position=(10, 120),
    width=180,
    height=6,
)

radius_slider = sliders.Slider(
    value=RADIUS,
    min=2,
    max=20,
    name="Radius",
    position=(10, 190),
    width=180,
    height=6,
)

roughness_slider = sliders.Slider(
    value=ROUGHNESS,
    min=0,
    max=10,
    name="Friction",
    position=(10, 260),
    width=180,
    height=6,
)

clear_button = Button("Clear", (50, HEIGHT - 80))

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] >= PANEL_WIDTH:
                add_object(
                    (event.pos[0] - PANEL_WIDTH, event.pos[1]),
                    mass=mass_slider.value,
                    radius=int(radius_slider.value),
                    roughness=roughness_slider.value,
                    elasticity=elasticity_slider.value,
                )
        elasticity_slider.handle_event(event)
        mass_slider.handle_event(event)
        radius_slider.handle_event(event)
        roughness_slider.handle_event(event)
        clear_button.handle_click(event, bodies_list, physic.space, sprites)

    physic.step(1 / FPS)
    sprites.update()

    side_panel.fill((50, 50, 50))
    main_area.fill((135, 206, 235))

    # Ground
    ground_rect = pygame.Rect(
        0, HEIGHT - GROUND_HEIGHT, WIDTH - PANEL_WIDTH, GROUND_HEIGHT
    )
    pygame.draw.rect(main_area, (101, 67, 33), ground_rect)

    sprites.draw(main_area)

    elasticity_slider.draw(side_panel)
    mass_slider.draw(side_panel)
    radius_slider.draw(side_panel)
    roughness_slider.draw(side_panel)
    clear_button.draw(side_panel)

    screen.blit(side_panel, (0, 0))
    screen.blit(main_area, (PANEL_WIDTH, 0))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
