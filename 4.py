f = 100000 #236491
t = 999999 #713787

def checkNumber(x):
	n = str(x)

	repeat = False
	increasing = True

	repeated = 0

	last = None

	for i in n:
		if last != None:
			if last == i:
				repeated += 1
			else:
				repeat = repeat or repeated == 1
				repeated = 0  
			increasing = increasing and int(last) <= int(i)

		last = i

	repeat = repeat or repeated == 1

	return repeat and increasing

q = 0

for i in range(f,t):
	if checkNumber(i):
		q += 1

print(q)