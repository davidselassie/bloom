from OpenGL.GL import *

import copy
import random

import bloom_engine
import bloom_entity
import bloom_vector

class bloomBackground:
	def __init__(self, speed, color, number):
		self.speed = speed
		self.color = color
		
		self.stars = [[random.random() * bloom_engine.space[0], random.random() * bloom_engine.space[1]] for num in xrange(0, number)]
				
	def update(self, dt):
		for star in self.stars:
			if star[1] < 0:
				star[1] = random.random() * 10 + 100
				star[0] = random.random() * 100
			else:
				star[1] += self.speed * dt
		
	def draw(self):
		glPushMatrix()
		
		glColor4fv(self.color)
		glBegin(GL_POINTS)
		for star in self.stars:
			glVertex2fv(star)
		glEnd()
			
		glPopMatrix()