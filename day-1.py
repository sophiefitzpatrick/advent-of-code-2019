# Advent of Code 2019 - Day 1

from input import masses
import math

# part 1
def fuel_requirement(masses):
	fuels = []

	for m in masses:
		fuel = math.floor(m/3) - 2
		fuels.append(fuel)

	return fuels

fuel_required = fuel_requirement(masses=masses)
print(sum(fuel_required))

# answer: 3376997

# part 2
def extra_fuel(mass):
	# value of fuel_required is the higher value between mass and 0
	fuel_required = max(math.floor(mass/3) - 2, 0)
	if fuel_required == 0:
		return 0
	return fuel_required + extra_fuel(fuel_required)

total_fuel = [extra_fuel(m) for m in masses]
print(sum(total_fuel))

# answer: 5062623