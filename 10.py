import math

input_string = """.###.###.###.#####.#
#####.##.###..###..#
.#...####.###.######
######.###.####.####
#####..###..########
#.##.###########.#.#
##.###.######..#.#.#
.#.##.###.#.####.###
##..#.#.##.#########
###.#######.###..##.
###.###.##.##..####.
.##.####.##########.
#######.##.###.#####
#####.##..####.#####
##.#.#####.##.#.#..#
###########.#######.
#.##..#####.#####..#
#####..#####.###.###
####.#.############.
####.#.#.##########."""

map = [[] for i in input_string.split()]
for i in range(len(map)):
	map[i] = list(input_string.split()[i])

maxX = 8
maxY = 16

def getAsteroids(x, y):
	n = 0
	angles = {}
	for y2, l in enumerate(map):
		for x2, c in enumerate(l):
			if c != ".":
				angle = math.degrees(math.atan2(y2 - y, x2 - x))
				if angle != 0 or (y2 == y and x < x2):
					angles[angle] = [x2,y2]
	return angles

def getAngles():
	return sorted (getAsteroids(maxX, maxY).keys())

angles = getAngles()

print(angles)
