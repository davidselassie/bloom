import pygame
from pygame.locals import *
from OpenGL.GL import *

import bloom_bind
import bloom_entity

# The screen is always 100 x 100 units.
space = (100, 100)
thickness = 5.0

class bloomEngine:
	def __init__(self, size, name, flags):
		pygame.init()
		self.ratio = 1.0
		
		self.window = pygame.display.set_mode(size, flags | DOUBLEBUF | HWSURFACE | OPENGL | RESIZABLE)
		pygame.display.set_caption(name)
		
		self.resize(size)
		
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glLineWidth(thickness)
		glPointSize(thickness)
		glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
		glEnable(GL_LINE_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		
		self.binds = []
		
		self.dt = 0
		self.time = pygame.time.get_ticks()
		self.frames = 0
		
	def update(self):
		self.dt = pygame.time.get_ticks() - self.time
		self.time = pygame.time.get_ticks()
		
		for bind in self.binds:
			bind.value = 0
		
		keys = pygame.key.get_pressed()
		for bind in self.binds:
			if not bind.wait and keys[bind.key]:
				bind.value += 1
		
		for event in pygame.event.get():
			if event.type == VIDEORESIZE:
				self.resize((event.w, event.h))
			for bind in self.binds:
				if bind.wait:
					if event.type == bind.key:
						bind.value += 1
					elif event.type == KEYDOWN and event.key == bind.key:
						bind.value += 1
		
	def bind(self, key, name, wait):
		self.binds.append(bloom_bind.bloomBind(key, name, wait))
		
	def resize(self, size):
		small_end = min(size)
		large_end = max(size)
		
		glViewport((large_end - small_end) / 2, 0, small_end, small_end)
		
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0, 100, 0, 100, -1, 1)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		
		thickness = small_end / 1024 * 5.0
		
	def checkBind(self, name):
		value = 0
		for bind in self.binds:
			if bind.name == name:
				value += bind.value
				
		return value
				
	def startDraw(self):
		self.frames = self.frames + 1
		glClear(GL_COLOR_BUFFER_BIT)
		
	def endDraw(self):
		glFlush()
		pygame.display.flip()
		
	def fps(self):
		return self.frames / (self.time / 1000.0)
		
