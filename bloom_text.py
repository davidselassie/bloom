from OpenGL.GL import *

import bloom_vector

textLists = glGenLists(57)

glNewList(textLists, GL_COMPILE) # Space
glEndList()

glNewList(textLists + 14, GL_COMPILE) # .
glBegin(GL_POINTS)
glVertex2f(0.0, -0.6)
glEnd()
glEndList()

glNewList(textLists + 16, GL_COMPILE) # 0
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
# Cross
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 17, GL_COMPILE) # 1
glBegin(GL_LINES)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 18, GL_COMPILE) # 2
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 19, GL_COMPILE) # 3
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 20, GL_COMPILE) # 4
glBegin(GL_LINES)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
glEnd()
glEndList()

glNewList(textLists + 21, GL_COMPILE) # 5
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 22, GL_COMPILE) # 6
glBegin(GL_LINES)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 23, GL_COMPILE) # 7
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 24, GL_COMPILE) # 8
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 25, GL_COMPILE) # 9
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 26, GL_COMPILE) # :
glBegin(GL_POINTS)
glVertex2f(0.0, 0.6)
glVertex2f(0.0, -0.6)
glEnd()
glEndList()

glNewList(textLists + 35, GL_COMPILE) # C
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 37, GL_COMPILE) # E
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 38, GL_COMPILE) # F
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
glEnd()
glEndList()

glNewList(textLists + 40, GL_COMPILE) # H
glBegin(GL_LINES)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 41, GL_COMPILE) # I
glBegin(GL_LINES)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 47, GL_COMPILE) # O
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 48, GL_COMPILE) # P
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
glEnd()
glEndList()

glNewList(textLists + 50, GL_COMPILE) # R
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Left Bottom
glVertex2f(-0.5, 0.0)
glVertex2f(-0.5, -1.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Top
glVertex2f(0.5, 1.0)
glVertex2f(0.5, 0.0)
# Bottom Right Slash
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

glNewList(textLists + 51, GL_COMPILE) # S
glBegin(GL_LINES)
# Top
glVertex2f(-0.5, 1.0)
glVertex2f(0.5, 1.0)
# Left Top
glVertex2f(-0.5, 1.0)
glVertex2f(-0.5, 0.0)
# Center
glVertex2f(-0.5, 0.0)
glVertex2f(0.5, 0.0)
# Right Bottom
glVertex2f(0.5, 0.0)
glVertex2f(0.5, -1.0)
# Bottom
glVertex2f(-0.5, -1.0)
glVertex2f(0.5, -1.0)
glEnd()
glEndList()

class bloomText:
    def __init__(self, string):
        self.string = string
        self.position = (0, 0)

    def draw(self):
        glPushMatrix()

        glTranslatef(self.position[0], self.position[1], 0.0)
        glColor4f(1.0, 1.0, 1.0, 1.0)

        for character in self.string:
            glCallList(textLists + ord(character) - 32) # 32 is Space
            glTranslatef(2.0, 0.0, 0.0)

        glPopMatrix()