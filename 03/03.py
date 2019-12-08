def manhattan_distance(x, y):
    return abs(x) + abs(y)

# Map which x/y values change by what value for a given direction.
deltas = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

# Get the coordinate points for a given wire.
def find_points(wire):
    points = set()
    paths = wire.split(',')
    x, y, steps = 0, 0, 0
    number_of_steps = {}
    for path in paths:
        direction = path[:1]
        length = int(path[1:])
        deltaX, deltaY = deltas[direction]
        while length > 0:
            length -= 1
            x += deltaX
            y += deltaY
            points.add((x, y))
            steps += 1
            number_of_steps.setdefault((x, y), steps)
    return points, number_of_steps

# Puzzle input.
with open('input') as puzzleInput:
    wires = [value for value in puzzleInput.read().splitlines()]

points_wire_1, number_of_steps_wire1 = find_points(wires[0])
points_wire_2, number_of_steps_wire2 = find_points(wires[1])

# We only care about where both wire 1 and wire 2 cross paths.
intersections = points_wire_1 & points_wire_2

# Figure out the closest intersection.
distances = [manhattan_distance(x, y) for x, y in intersections]

# Part 1 answer.
print(min(distances))

# The combined steps the wires must take to reach an intersection.
steps = [number_of_steps_wire1[(x, y)] + number_of_steps_wire2[(x, y)] for x, y in intersections]

# Part 2 answer
print(min(steps))
