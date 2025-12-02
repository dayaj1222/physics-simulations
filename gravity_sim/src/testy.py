import pygame

from gravity_sim import sliders

# --- Settings ---
WIDTH, HEIGHT = 800, 600
FPS = 60
RUNNING = True

# --- Initialize Pygame ---
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")
clock = pygame.time.Clock()

slider = sliders.Slider(
    value=5.0,
    min=0,
    max=10,
    name="Elasticity",
    position=(100, 200),
    width=200,
    height=6,
)


# --- Main Loop ---
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        slider.handle_event(event)

    # --- Update Game State ---
    # (update objects, physics, etc.)

    # --- Draw ---
    screen.fill((0, 0, 0))  # fill screen with black
    # draw your objects here
    slider.draw(screen)

    pygame.display.flip()  # update the display
    clock.tick(FPS)

pygame.quit()
