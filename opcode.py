import math

# Day 11
out = []
pos = [0, 0]
direction = 0

panel = {(0, 0) : 1}

def rotate(d):
	global direction
	direction += d - 1 + d
	if direction < 0:
		direction = 3
	if direction > 3:
		direction = 0

	if direction == 0:
		pos[1] -= 1
	if direction == 1:
		pos[0] += 1
	if direction == 2:
		pos[1] += 1
	if direction == 3:
		pos[0] -= 1

def paint():
	global out
	panel[ (pos[0], pos[1]) ] = out[0]

	rotate(out[1])

	out = []

def fillMemory(code, v):
	for i in range(len(code), v + 1):
		code.append(0)

def getModes(x):
	m = [0,0,0,0]
	
	m[0] = x % 100
	x = math.floor(x/100)

	for i in range(1,4):
		m[i] = x%10
		x = math.floor(x/10)

	return m

def getParameter(value, mode, code, rel):
	if len(code) <= value and mode != 1:
		fillMemory(code, value)
	if mode == 0:
		return code[value]
	elif mode == 1:
		return value
	elif mode == 2:
		return code[value + rel]

def calculate(c):
	code = c[:]
	i = 0
	ins = 0
	rel = 0
	while code[i] != 99:
		m = getModes(code[i])

		if m[0] == 1:
			p1 = getParameter(code[i+1], m[1], code, rel)
			p2 = getParameter(code[i+2], m[2], code, rel)
			to = code[i+3]#getParameter(code[i+3], m[3], code, rel)
			if m[3] == 2:
				to = rel + code[i+3]
			if to >= len(code):
				fillMemory(code, to)

			code[to] = p1 + p2
			i += 4

		if m[0] == 2:
			p1 = getParameter(code[i+1], m[1], code, rel)
			p2 = getParameter(code[i+2], m[2], code, rel)
			to = code[i+3]
			if m[3] == 2:
				to = rel + code[i+3]
			if to >= len(code):
				fillMemory(code, to)
			code[to] = p1 * p2
			i += 4

		if m[0] == 3:
			to = code[i+1]#getParameter(code[i+1], m[1], code, rel)
			if m[1] == 2:
				to = rel + code[i+1]
			p = 0
			if (pos[0], pos[1]) in panel:
				p = panel[(pos[0], pos[1])]
			code[to] = p
			#code[to] = inp[ins]
			#ins += 1
			i += 2

		if m[0] == 4:
			to = getParameter(code[i+1], m[1], code, rel)
			out.append(to)
			i += 2

		if m[0] == 5:
			p1 = getParameter(code[i+1], m[1], code, rel)
			to = getParameter(code[i+2], m[2], code, rel)
			if to >= len(code):
				fillMemory(code, to)

			if p1 != 0:
				i = to
			else:
				i += 3

		if m[0] == 6:
			p1 = getParameter(code[i+1], m[1], code, rel)
			to = getParameter(code[i+2], m[2], code, rel)
			if to >= len(code):
				fillMemory(code, to)

			if p1 == 0:
				i = to
			else:
				i+= 3

		if m[0] == 7:
			p1 = getParameter(code[i+1], m[1], code, rel)
			p2 = getParameter(code[i+2], m[2], code, rel)
			to = code[i+3]
			if m[3] == 2:
				to = rel + code[i+3]
			if to >= len(code):
				fillMemory(code, to)

			if p1 < p2:
				code[to] = 1
			else:
				code[to] = 0

			i += 4

		if m[0] == 8:
			p1 = getParameter(code[i+1], m[1], code, rel)
			p2 = getParameter(code[i+2], m[2], code, rel)
			to = code[i+3]
			if m[3] == 2:
				to = rel + code[i+3]
			if to >= len(code):
				fillMemory(code, to)

			if p1 == p2:
				code[to] = 1
			else:
				code[to] = 0

			i += 4

		if m[0] == 9:
			p1 = getParameter(code[i+1], m[1], code, rel)
			rel += p1

			i += 2

		#Day 11
		if len(out) == 2:
			paint()

	#return out
	return panel