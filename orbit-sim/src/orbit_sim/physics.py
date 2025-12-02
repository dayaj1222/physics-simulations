from pygame import Vector2

from orbit_sim.bodies import Body

G = 3


class PhysicsEngine:
    def __init__(self, bodies: list[Body]) -> None:
        self.bodies = bodies

    def apply_gravity(self, dt):
        for body_a in self.bodies:
            others = [b for b in self.bodies if b is not body_a]
            acceleration = Vector2()

            for body_b in others:
                r_vec = body_b.position - body_a.position
                distance_squared = r_vec.length_squared()

                if distance_squared > 0.1:
                    acceleration += (
                        G * body_b.mass / distance_squared * r_vec.normalize()
                    )

            body_a.velocity += acceleration * dt

    def apply_collision_detection(self):
        checked_pairs = set()

        for body_a in self.bodies:
            for body_b in self.bodies:
                if body_a is body_b:
                    continue

                pair = tuple(sorted([id(body_a), id(body_b)]))
                if pair in checked_pairs:
                    continue
                checked_pairs.add(pair)

                distance = body_a.position.distance_to(body_b.position)
                sum_of_radius = body_a.radius + body_b.radius

                if distance < sum_of_radius:
                    # Separate overlapping bodies
                    overlap = sum_of_radius - distance
                    direction = (body_b.position - body_a.position).normalize()

                    body_a.position -= direction * (overlap / 2)
                    body_b.position += direction * (overlap / 2)

                    # Elastic collision (conserves momentum)
                    v_rel = body_a.velocity - body_b.velocity
                    v_norm = v_rel.dot(direction)

                    # Only collide if moving toward each other
                    if v_norm > 0:
                        mass_sum = body_a.mass + body_b.mass

                        impulse = (2 * v_norm) / mass_sum

                        body_a.velocity -= impulse * body_b.mass * direction
                        body_b.velocity += impulse * body_a.mass * direction
