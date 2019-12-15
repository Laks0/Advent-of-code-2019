input_string = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

extra = {}
ore = 0
totalReq = []

ingredients = {}
instructions = [str(i) for i in input_string.split("\n")]
for i, n in enumerate(instructions):
	instructions[i] = n.split(" => ")
	a = instructions[i][1].split(" ")
	ingredients[a[1]] = [int(a[0]), instructions[i][0].split(", ")]

def multRecipe(r, t):
	nr = []
	for i in r:
		a = i.split()
		nr.append(str(int(a[0]) * t) + " " + a[1])

	return nr

def getIngredients(s):
	q = int(s.split()[0])
	oq = q
	i = s.split()[1]

	if i in extra:
		q -= extra[i]
	else:
		extra[i] = 0

	if q <= 0:
		extra[i] -= oq
		return None

	extra[i] = 0

	recipe = ingredients[i]
	t = 1
	while recipe[0] * t < q:
		t += 1
	extra[i] += recipe[0] * t - q

	return multRecipe(recipe[1], t)

totalReq = getIngredients("1 FUEL")

while len(totalReq) > 0:
	toAdd = []
	toRemove = []
	for i in totalReq:
		if i.split()[1] != "ORE":
			ing = getIngredients(i)
			if ing != None:
				for x in ing:	
					toAdd.append(x)
			toRemove.append(i)

	for i in toRemove:
		totalReq.remove(i)
	for i in toAdd:
		totalReq.append(i)

	for i in totalReq:
		if i.split()[1] == "ORE":
			ore += int(i.split()[0])
			totalReq.remove(i)

print(ore)