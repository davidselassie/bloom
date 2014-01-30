import copy
from OpenGL.GL import *
import math

import bloom_entity

bulletLists = glGenLists(2)

glNewList(bulletLists, GL_COMPILE)
#glColor4f(0.0, 1.0, 0.0, 1.0)
glBegin(GL_LINE_LOOP)
glVertex2f(-1.0, 1.5)
glVertex2f(1.0, 1.5)
glVertex2f(1.0, -1.5)
glVertex2f(-1.0, -1.5)
glEnd()
#glColor4f(0.0, 1.0, 0.0, 0.5)
glBegin(GL_QUADS)
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
glVertex2f(0.5, -1.0)
glVertex2f(-0.5, -1.0)
glEnd()
glEndList()

glNewList(bulletLists + 1, GL_COMPILE)
#glColor4f(0.0, 0.0, 1.0, 1.0)
glBegin(GL_LINE_LOOP)
glVertex2f(-1.0, 1.0)
glVertex2f(1.0, 1.0)
glVertex2f(1.0, -1.0)
glVertex2f(-1.0, -1.0)
glEnd()
#glColor4f(0.0, 0.0, 1.0, 0.5)
glBegin(GL_QUADS)
glVertex2f(-1.0, 1.0)
glVertex2f(1.0, 1.0)
glVertex2f(1.0, -1.0)
glVertex2f(-1.0, -1.0)
glEnd()
glEndList()

powerList = (1.0, 1.0)
sizeList = (1.5, 1.0)
speedList = (0.2, 0.05)

class bloomBullet(bloom_entity.bloomEntity):
    def __init__(self, position, direction, team, style):
        bloom_entity.bloomEntity.__init__(self, position)
        self.speed = speedList[style]
        self.velocity = direction.unit() * self.speed
        self.team = team
        self.power = powerList[style]
        self.size = sizeList[style]
        self.rotation_velocity = 0.0
        self.style = style

    def draw(self):
        glPushMatrix()

        glTranslatef(self.position[0], self.position[1], 0.0)
        glRotatef(self.rotation, 0.0, 0.0, 1.0)
        glColor4fv(self.color)

        glCallList(bulletLists + self.style)

        glPopMatrix()
