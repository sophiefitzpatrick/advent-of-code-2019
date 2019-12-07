# Advent of Code 2019 - Day 3

wire1 = open("wire_1.txt", "r").read().split(",")
wire2 = open("wire_2.txt", "r").read().split(",")

def smallest_distance_crossed_wires(wire, area, delay, wire_id, is_delayed=False):
    move = 0
    smallest_distance = 100000000
    x, y = 0, 0

    for index in range(len(wire)):
        instruction = wire[index]
        direction = instruction[0:1]
        number_of_moves = instruction[1:]
        for move in range(int(number_of_moves)):
            if direction == 'R':
                x = x + 1
            elif direction == 'U':
                y = y + 1
            elif direction == 'L':
                x = x - 1
            elif direction == 'D':
                y = y - 1
            else:
                print("bippity boppity boop")
            move = move + 1
            key = "%s, %s" % (x, y)
            if area.get(key) is None:
            	area[key] = wire_id
            	delay[key] = move
            else:
            	smallest_distance = min(smallest_distance, delay.get(key) + move if is_delayed else abs(x) + abs(y))

    return smallest_distance

def manhattan_distance():
	area = {}
	delay = {}
	smallest_distance_crossed_wires(wire1, area, delay, 1)
	return smallest_distance_crossed_wires(wire2, area, delay, 2)

result = manhattan_distance()
print(result)

# method not working rip.
def minimise_signal_display():
	area = {}
	delay = {}
	smallest_distance_crossed_wires(wire1, area, delay, 1, is_delayed=True)
	return smallest_distance_crossed_wires(wire2, area, delay, 2, is_delayed=True)

print(minimise_signal_display())
