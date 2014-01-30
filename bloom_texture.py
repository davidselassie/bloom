import pygame
import Image
import math

from OpenGL.GL import *

class bloomTexture:
	def __init__(self):
		self.textureID = 0
		self.size = (0, 0)
		
	def __del__(self):
		glDeleteTextures([self.textureID])
		
	def load(self, filename):
		image = Image.open(filename)
		
		self.size = map(self.nearest2, image.size)
		image = image.resize(self.size, Image.BILINEAR)
		image = image.transpose(Image.FLIP_TOP_BOTTOM)
		
		self.textureID = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

# Image module doesn't support alpha.
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.size[0], self.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image.tostring("raw", "RGB"))
		
	def nearest2(self, number):
		power = 2 ** int(math.log(number, 2))
		if power > glGetIntegerv(GL_MAX_TEXTURE_SIZE):
			return glGetIntegerv(GL_MAX_TEXTURE_SIZE)
		return power
		
	def blank(self, size):
		glEnable(GL_TEXTURE_2D)
		self.size = map(self.nearest2, size)
		surface = pygame.Surface(self.size)
	
		self.textureID = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.size[0], self.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(surface, "RGBA"))
		
	def bind(self):
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		
	def startRender(self):
		self.old_viewport = glGetIntegerv(GL_VIEWPORT)
		glViewport(0, 0, self.size[0], self.size[1])
	
	def endRender(self):
		glBindTexture(GL_TEXTURE_2D, self.textureID)
		glCopyTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 0, 0, self.size[0], self.size[1], 0)
		glViewport(self.old_viewport[0], self.old_viewport[1], self.old_viewport[2], self.old_viewport[3])
		