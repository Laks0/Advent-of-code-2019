import numpy
import math

class Planet:
	def __init__(self, x, y, z):
		self.pos = numpy.array([x, y, z])
		self.vel = numpy.array([0, 0, 0])

	def move(self):
		self.pos += self.vel

	def setGravity(self, p2):
		for i in range(3):
			if self.pos[i] < p2[i]:
				self.vel[i] += 1
			elif self.pos[i] != p2[i]:
				self.vel[i] -= 1

	def getEergy(self):
		pot = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
		kin = abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])
		return pot * kin

inputs = [
	[1, 4, 4],
	[-4, -1, 19],
	[-15, -14, 12],
	[-17, 1, 10]
]

inputs = [
	[-1, 0, 2],
	[2, -10, -7],
	[4, -8, 8],
	[3, 5, -1]
]

planets = []

for i in range(4):
	inp = inputs[i]
	x = inp[0]
	y = inp[1]
	z = inp[2]
	planets.append(Planet(x, y, z))

def changeVelocities():
	for i, p in enumerate(planets):
		for l, p2 in enumerate(planets):
			if i != l:
				planets[i].setGravity(p2.pos)

i = 1
while 1:
	back = True
	changeVelocities()
	for l, p in enumerate(planets):
		if i != 0:
			back = back and (p.pos == inputs[l]).all() and (p.vel == [0, 0, 0]).all()
		else:
			back = False
		p.move()
	if back:
		break
	i += 1

print(i)