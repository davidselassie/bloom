import copy
import random
from OpenGL.GL import *

import bloom_entity
import bloom_barrage
import bloom_bullet
import bloom_explosion
import bloom_vector

styleList = glGenLists(2)

glNewList(styleList, GL_COMPILE)
glBegin(GL_LINE_LOOP)
glVertex2f(-1.0, 1.0)
glVertex2f(1.0, 0.0)
glVertex2f(-1.0, -1.0)
glEnd()
glEndList()

glNewList(styleList + 1, GL_COMPILE)
glBegin(GL_LINE_LOOP)
glVertex2f(-1.0, 1.0)
glVertex2f(1.0, 1.0)
glVertex2f(1.0, -1.0)
glVertex2f(-1.0, -1.0)
glEnd()
glEndList()

#styles = [[listID => st], []

class bloomShip(bloom_entity.bloomEntity):
    def __init__(self, position, team, style):
        bloom_entity.bloomEntity.__init__(self, position)

        self.color = [1.0, 0.0, 0.0, 1.0]
        self.speed = 0.06
        self.fire_speed = 25
        self.bullet_speed = 0.2
        self.last_fire = 0
        self.team = team
        self.health = self.total_health = float(10)
        self.size = 1.0
        self.style = style
#        self.barrage = barrage.Barrage()
#        self.barrage.addBullet(bullet.Bullet())

    def fire(self):
        newBullets = []
        if self.life_time - self.last_fire > self.fire_speed:
            self.last_fire = self.life_time
            newBullet = bloom_bullet.bloomBullet(copy.deepcopy(self.position), bloom_vector.bloomVector(0.0, 1.0), self.team, 0)
            newBullet.color = self.color
            newBullets += [newBullet]

        return newBullets

    def checkBullets(self, bullets):
        for bullet in bullets:
            if bullet.team != self.team and self.checkHitFast(bullet):
                self.health -= bullet.power
                bullets.remove(bullet)

    def dead(self):
        return self.health <= 0

    def explode(self):
        return [bloom_explosion.bloomExplosion(self.position + [random.randint(-2, 2), random.randint(-2, 2)], self.style) for number in range(0, 10)]

    def draw(self):
        glPushMatrix()

        glTranslatef(self.position[0], self.position[1], 0.0)
        glColor4fv(self.color)

        glCallList(styleList + self.style)

        glPopMatrix()