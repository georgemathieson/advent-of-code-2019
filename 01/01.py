from math import floor

# Calculate the fuel required for a given modules mass.
def calculate_fuel(mass):
    return int(floor(mass / 3) - 2)

# Given examples.
assert calculate_fuel(12) == 2
assert calculate_fuel(14) == 2
assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583

# Puzzle input.
with open('input') as puzzleInput:
    data = [int(mass) for mass in puzzleInput]

# Check puzzle data.
assert data[0] == 50062
assert len(data) == 100

# Calculate part 1.
part1 = sum(calculate_fuel(mass) for mass in data)
print('part 1:')
print(part1)

# Take into account that fuel itself requires fuel.
def calculate_fuel_including_fuel(mass):
    returnValue = 0
    fuel = calculate_fuel(mass)
    if (fuel >= 0):
        returnValue = fuel + calculate_fuel_including_fuel(fuel)
    return returnValue

# Given examples for part 2.
assert calculate_fuel_including_fuel(12) == 2
assert calculate_fuel_including_fuel(14) == 2
assert calculate_fuel_including_fuel(1969) == 966
assert calculate_fuel_including_fuel(100756) == 50346

# Calculate part 2.
part2 = sum(calculate_fuel_including_fuel(mass) for mass in data)
print('part 2:')
print(part2)
