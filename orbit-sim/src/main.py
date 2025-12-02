import os

import pygame
from pygame import Vector2, sprite

from orbit_sim.bodies import Body
from orbit_sim.physics import PhysicsEngine

os.environ["SDL_VIDEO_WINDOW_POS"] = "1000,0"


def main():
    pygame.init()
    HEIGHT = 800
    WIDTH = 1200

    planets = sprite.Group()

    sun = Body(
        mass=15000,
        radius=50,
        position=Vector2(600, 400),
        velocity=Vector2(0, 0),
        image_path="./assets/pngegg (7).bmp",
    )

    planet1 = Body(
        mass=10,
        radius=12,
        position=Vector2(600, 250),
        velocity=Vector2(18, 0),
        image_path="./assets/pngegg (1).bmp",
    )

    planet2 = Body(
        mass=15,
        radius=15,
        position=Vector2(600, 200),
        velocity=Vector2(15, 0),
        image_path="./assets/pngegg (2).bmp",
    )

    planet3 = Body(
        mass=12,
        radius=13,
        position=Vector2(600, 150),
        velocity=Vector2(13, 0),
        image_path="./assets/pngegg (3).bmp",
    )

    planet4 = Body(
        mass=20,
        radius=18,
        position=Vector2(600, 100),
        velocity=Vector2(11, 0),
        image_path="./assets/pngegg (4).bmp",
    )

    planet5 = Body(
        mass=8,
        radius=10,
        position=Vector2(600, 50),
        velocity=Vector2(10, 0),
        image_path="./assets/pngegg (5).bmp",
    )

    planet6 = Body(
        mass=5,
        radius=8,
        position=Vector2(600, 650),
        velocity=Vector2(-10, 0),
        image_path="./assets/pngegg (6).bmp",
    )

    physics_engine = PhysicsEngine(
        [sun, planet1, planet2, planet3, planet4, planet5, planet6]
    )
    planets.add(sun, planet1, planet2, planet3, planet4, planet5, planet6)

    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        dt = clock.tick(60) / 100

        physics_engine.apply_gravity(dt)
        physics_engine.apply_collision_detection()
        planets.update(dt)
        planets.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
