from OpenGL.GL import *

import bloom_engine

import bloom_entity
import bloom_ship
import bloom_aiship
import bloom_bullet
import bloom_explosion
import bloom_background
import bloom_texture
import bloom_vector

class bloomLevel:
    def __init__(self):
        self.ships = []
        self.bullets = []
        self.explosions = []

        self.backgrounds = [bloom_background.bloomBackground(-0.001, [0.1, 0.1, 0.1, 1.0], 400),
            bloom_background.bloomBackground(-0.0025, [0.25, 0.25, 0.25, 1.0], 200),
            bloom_background.bloomBackground(-0.005, [0.5, 0.5, 0.5, 1.0], 100),
            bloom_background.bloomBackground(-0.01, [1.0, 1.0, 1.0, 1.0], 50)]

        self.bloom = bloom_texture.bloomTexture()
        self.bloom.blank((64, 64))

    def update(self, dt):
        for background in self.backgrounds:
            background.update(dt)

        for bullet in self.bullets:
            bullet.update(dt)
            if bullet.offScreen() == 2:
                self.bullets.remove(bullet)

        for ship in self.ships:
            ship.checkBullets(self.bullets)
            if ship.health <= 0:
                self.explosions += ship.explode()
                self.ships.remove(ship)
                continue
            ship.fire()
            ship.update(dt)
#            if type(ship) == bloom_aiship.bloomAIShip

        for explo in self.explosions:
            explo.update(dt)
            if explo.life_time > explo.length:
                self.explosions.remove(explo)

    def draw(self):
        for background in self.backgrounds:
            background.draw()

        for ship in self.ships:
            ship.draw()

        for bullet in self.bullets:
            bullet.color[3] = 1.0# - bullet.life_time / 600.0
            bullet.draw()

        for explosion in self.explosions:
            explosion.draw()

        glPushMatrix()

        glEnable(GL_TEXTURE_2D)
        self.bloom.bind()
        glColor4f(1.0, 1.0, 1.0, 0.8)

        glBegin(GL_QUADS)

        glTexCoord2f(0.0, 0.0)
        glVertex2f(0.0, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(bloom_engine.space[0], 0.0)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(bloom_engine.space[0], bloom_engine.space[1])
        glTexCoord2f(0.0, 1.0)
        glVertex2f(0.0, bloom_engine.space[1])

        glEnd()
        glDisable(GL_TEXTURE_2D)

        glPopMatrix()

    def drawBloom(self):
        self.bloom.startRender()
        glDisable(GL_LINE_SMOOTH)
        glClear(GL_COLOR_BUFFER_BIT)
        glLineWidth(1.0)
        glPointSize(1.0)

#        for background in self.backgrounds:
#            background.draw()

        for bullet in self.bullets:
            bullet.color[3] = bullet.life_time / 300.0
            bullet.draw()

        for explosion in self.explosions:
            explosion.draw()

        self.bloom.endRender()
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(bloom_engine.thickness)
        glPointSize(bloom_engine.thickness)
        glFlush()
