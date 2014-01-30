from OpenGL.GL import *
import copy

import bloom_engine
import bloom_vector

class bloomEntity:
    def __init__(self, position):
        self.position = position
        self.old_position = copy.deepcopy(self.position)

        self.velocity = bloom_vector.bloomVector(0.0, 0.0)
        self.acceleration = bloom_vector.bloomVector(0.0, 0.0)

        self.rotation = 0.0
        self.rotation_velocity = 0.0
        self.rotation_acceleration = 0.0

        self.scale = 1.0
        self.color = [1.0, 1.0, 1.0, 1.0]

        self.size = 0.0

        self.life_time = 0

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.old_position = copy.deepcopy(self.position)

        self.position += self.velocity * dt
        self.rotation_velocity += self.rotation_acceleration * dt
        self.rotation += self.rotation_velocity * dt
        self.acceleration.zero()
        self.rotation_acceleration = 0.0
        self.life_time += dt

    def force(self, direction):
        self.acceleration += direction

    def spin(self, direction):
        self.rotation_acceleration += direction

    def move(self, direction):
        self.position += direction

    def rotate(self, amount):
        self.rotation += amount

    def checkHitFast(self, entity):
        if self.position.fastDistance(entity.position) <= (self.size + entity.size):
            return True
        return False

    def checkHit(self, entity):
        if self.position[0] == self.old_position[0]:
            return entity.position[1] <= self.old_position[1] and entity.position[1] >= self.position[1] and abs(self.position[0] - entity.position[0]) <= self.size + entity.size
        else:
            m = (self.position[1] - self.old_position[1]) / (self.position[0] - self.old_position[0])

            x_old = self.old_position[0] - entity.position[0]
            x = m ** 2 * x_old / (1 + m ** 2)

            return x ** 2 + (m * (x - x_old)) ** 2 <= (self.size + entity.size) ** 2

    def offScreen(self):
        if self.position[0] < -self.size \
            or self.position[0] > self.size + bloom_engine.space[0] \
            or self.position[1] < -self.size \
            or self.position[1] > self.size + bloom_engine.space[1]:
            return 2 # Totaly off
        elif self.position[0] - self.size < 0 \
            or self.position[0] + self.size > bloom_engine.space[0] \
            or self.position[1] - self.size < 0 \
            or self.position[1] + self.size > bloom_engine.space[1]:
            return 1 # Not all on

        return False

    def fitScreen(self):
        if self.position[0] - self.size < 0:
            self.position[0] = self.size
        elif self.position[0] + self.size > bloom_engine.space[0]:
            self.position[0] = bloom_engine.space[0] - self.size

        if self.position[1] - self.size < 0:
            self.position[1] = self.size
        elif self.position[1] + self.size > bloom_engine.space[1]:
            self.position[1] = bloom_engine.space[1] - self.size
