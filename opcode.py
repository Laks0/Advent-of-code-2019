import math

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

def calculate(c, inp):
	code = c[:]
	out = []
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
			code[to] = inp#inp[ins]
			ins += 1
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

	return out