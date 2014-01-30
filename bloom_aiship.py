import random
import math
import copy

import bloom_ship
import bloom_bullet
import bloom_vector

class bloomAIShip(bloom_ship.bloomShip):
    def __init__(self, position, team, style, target):
        bloom_ship.bloomShip.__init__(self, position, team, style)
        self.target = target

    def fire(self):
        newBullets = []
        if self.life_time - self.last_fire >= self.fire_speed:
            self.last_fire = self.life_time
            if self.target == None:
                newBullet = bloom_bullet.bloomBullet(copy.deepcopy(self.position), bloom_vector.bloomVector(0.0, 1.0), self.team, 1)
            else:
                newBullet = bloom_bullet.bloomBullet(copy.deepcopy(self.position), bloom_vector.bloomVector(self.target.position[0] - self.position[0], self.target.position[1] - self.position[1]), self.team, 1)
            newBullet.color = [0.0, 0.0, 1.0, 1.0]
            newBullets.append(newBullet)

        return newBullets

    def update(self, dt):
        self.position[0] = (math.cos(self.life_time / 1000.0) + 1) * 45
        self.position[1] = 100.0 - self.life_time / 9000.0 * 100.0

        bloom_ship.bloomShip.update(self, dt)