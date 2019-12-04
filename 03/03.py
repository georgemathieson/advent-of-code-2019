def manhattan_distance(x, y):
    return abs(x) + abs(y)


# Map which x/y values change for a given direction.
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
    x, y = 0, 0
    for path in paths:
        direction = path[:1]
        length = int(path[1:])
        deltaX, deltaY = deltas[direction]
        while length > 0:
            length -= 1
            x += deltaX
            y += deltaY
            points.add((x, y))
    return points

# Puzzle input.
with open('input') as puzzleInput:
    wires = [value for value in puzzleInput.read().splitlines()]

pointsWire1 = find_points(wires[0])
pointsWire2 = find_points(wires[1])

# We only care about where both wire 1 and wire 2 cross paths.
intersections = pointsWire1 & pointsWire2

# Figure out the closest intersection.
distances = []
for x, y in intersections:
    distances.append(manhattan_distance(x, y))

# Part 1 answer.
print(min(distances))
