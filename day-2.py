# Advent of Code 2019 - Day 2

from input import gravity_assist_programme

# part 1
def find_position_0(gap, pos_1, pos_2):
	# terminology is my own, refined in part 2
	position = 0
	gap[1] = pos_1
	gap[2] = pos_2

	while True:
		if gap[position] == 1:
			gap[gap[position + 3]] = gap[gap[position + 1]] + gap[gap[position + 2]]
			position = position + 4
		elif gap[position] == 2:
			gap[gap[position + 3]] = gap[gap[position + 1]] * gap[gap[position + 2]]
			position = position + 4
		elif gap[position] == 99:
			break
		else:
			print("i am <^..^>")

	return gap[0]

fixed_gravity_assist_programme = find_position_0(
	gap=gravity_assist_programme,
	pos_1=12,
	pos_2=2
)
print(fixed_gravity_assist_programme)

# answer: 10566835

# part 2

'''
memory = input as a list of integers
address = index in list
opcodes = 1, 2, 99 - mark the beginning of an instruction
parameters = 3 addresses after the opcode unless the opcode is 99
instruction pointer = address of current instruction, starting at 0
verb = index 2
noun = index 1
'''

def output_calculation(output):
	for noun in range(100):
		for verb in range(100):
			if find_position_0(gravity_assist_programme.copy(), noun, verb) == output:
				return 100 * noun + verb
	return 'boop'

print(output_calculation(output=19690720))

# answer: 2347
