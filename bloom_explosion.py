import copy
from OpenGL.GL import *
import random

import bloom_entity

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

class bloomExplosion(bloom_entity.bloomEntity):
	def __init__(self, position, style):
		bloom_entity.bloomEntity.__init__(self, position)
		
		self.length = 1000.0
		
		self.rotation_velocity = random.random() / 4.0
		
		self.style = style
	
	def draw(self):
		to0 = (self.length - self.life_time) / self.length
		glPushMatrix()
		
		glTranslatef(self.position[0], self.position[1], 0.0)
		if self.life_time != self.length:
			toInfinity = 1 / to0
			glScalef(toInfinity, toInfinity, 1.0)
		glRotate(self.rotation, 0.0, 0.0, 1.0)
		glColor4f(1.0, 0.7, 0.0, to0)
		
		glCallList(styleList + self.style)
		
		glPopMatrix()