from OpenGL.GL import *

class bloomModel:
	def __init__(self):
		pass
		
	def draw(self):
		if type(self) == bloomBullet:
			glBegin(GL_LINE_LOOP)
		
			glVertex2f(1.0, 0.0)
			glVertex2f(-1.0, 1.0)
			glVertex2f(-1.0, -1.0)
			
			glEnd()
		else:
			glBegin(GL_LINE_LOOP)
			
			glVertex2f(-1.0, 1.0)
			glVertex2f(1.0, 1.0)
			glVertex2f(1.0, -1.0)
			glVertex2f(-1.0, -1.0)
			
			glEnd()