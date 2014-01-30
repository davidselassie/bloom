#!/usr/bin/env python

import pygame, sys, os
from pygame.locals import *
import random
import pickle

from bloom_engine import *

engine = bloomEngine((800, 600), "Bloom", 0)

from bloom_vector import *
from bloom_level import *
from bloom_ship import *
from bloom_aiship import *
from bloom_text import *

level = bloomLevel()

playerShip = bloomShip(bloomVector(50, 25), 1, 1)
playerShip.color = [0.0, 1.0, 0.0, 1.0]
playerShip.total_health = 1
playerShip.health = 1

level.ships.append(playerShip)

engine.bind(QUIT, "quit", True)
engine.bind(K_ESCAPE, "quit", False)

engine.bind(K_n, "restart", True)

engine.bind(K_LMETA, "fire", False)
engine.bind(K_LEFT, "left", False)
engine.bind(K_RIGHT, "right", False)
engine.bind(K_UP, "up", False)
engine.bind(K_DOWN, "down", False)

engine.bind(K_LCTRL, "spawn", False)
engine.bind(K_LSHIFT, "swap", False)

lastTime = 0
score = 0
hiScore = 0
try:
	scoreFile = file("settings.pickle")
	hiScore = pickle.load(scoreFile)
	scoreFile.close()
except IOError:
	pass

scoreText = bloomText("SCORE: 0")
scoreText.position = (2, 2)
hiScoreText = bloomText("HI: " + str(hiScore))
hiScoreText.position = (50, 2)
fpsText = bloomText("FPS: 0")
fpsText.position = (2, 98)
while not engine.checkBind("quit"):
#	pygame.time.wait(80)
	engine.update()
	fpsText.string = "FPS: " + str(int(engine.fps()))

	if not playerShip.dead() and not engine.time // 1000 == lastTime:
#	if engine.checkBind("spawn"):
		lastTime = engine.time // 1000
		newEnemy = bloomAIShip(bloomVector(random.randint(5, bloom_engine.space[0] - 5), random.randint(25, bloom_engine.space[1] - 5)), 2, 0, playerShip)
		newEnemy.fire_speed = 1500
		level.ships.append(newEnemy)
		score += 1
		scoreText.string = "SCORE: " + str(score)

		if score > hiScore:
			hiScore = score
			hiScoreText.string = "HI: " + str(hiScore)

		print "level.ships" + str(len(level.ships))
		print "level.bullets" + str(len(level.bullets))
		print "level.explosions" + str(len(level.explosions))

	if engine.checkBind("restart"):
		score = 0
		scoreText.string = "SCORE: 0"
		level.__init__()
		playerShip = bloomShip(bloomVector(50, 25), 1, 1)
		playerShip.color = [0.0, 1.0, 0.0, 1.0]
		playerShip.total_health = 1
		playerShip.health = 1
		level.ships.append(playerShip)

	if not playerShip.dead():
		if engine.checkBind("left"):
			playerShip.move([-playerShip.speed * engine.dt, 0])
		if engine.checkBind("right"):
			playerShip.move([playerShip.speed * engine.dt, 0])
		if engine.checkBind("up"):
			playerShip.move([0, playerShip.speed * engine.dt])
		if engine.checkBind("down"):
			playerShip.move([0, -playerShip.speed * engine.dt])

		if playerShip.offScreen():
			playerShip.fitScreen()

		if not engine.checkBind("swap"):
			playerShip.fire_speed = 25
			playerShip.speed = 0.06
			playerShip.color = [0.0, 1.0, 0.0, 1.0]
		else:
			playerShip.fire_speed = 0
			playerShip.speed = 0.01
			playerShip.color = [1.0, 1.0, 0.0, 1.0]

		if engine.checkBind("fire"):
			level.bullets += playerShip.fire()

	level.update(engine.dt)

# Begin Drawing
	level.drawBloom()

	engine.startDraw()

	level.draw()

	scoreText.draw()
	fpsText.draw()
	hiScoreText.draw()

	engine.endDraw()
# End Drawing

try:
	scoreFile = file("settings.pickle", "w")
	pickle.dump(hiScore, scoreFile)
	scoreFile.close()
except IOError:
	pass
