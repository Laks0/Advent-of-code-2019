input_string = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0"
input_array = [int(i) for i in input_string.split(",")]

def calculate(input):
	i = 0
	while input[i] != 99:
		if input[i] == 1:
			input[input[i+3]] = input[input[i+2]] + input[input[i+1]]
			i += 4
		if input[i] == 2:
			input[input[i+3]] = input[input[i+2]] * input[input[i+1]]
			i += 4
		else:
			i += 1
	return(input)

def bf():
	noun = 0
	while noun <= 99:
		verb = 0
		while verb <= 99:
			copy = input_array[:]
			copy[1] = noun
			copy[2] = verb

			x = calculate(copy)[0]

			if x == 19690720:
				return 100 * noun + verb
			verb += 1
		noun += 1

#print(bf())