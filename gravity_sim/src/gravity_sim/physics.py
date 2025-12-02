from typing import Tuple

import pymunk

from gravity_sim.bodies import Body


class Physics:
    def __init__(self, gravity: Tuple[int, int], bodies: list[Body]) -> None:
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.bodies = bodies

    def apply_physics(self):
        for body in self.bodies:
            self.space.add(body.physics_body, body.shape)

    def step(self, dt: float):
        self.space.step(dt)
