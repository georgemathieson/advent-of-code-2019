import re

# Puzzle input.
with open('input') as puzzleInput:
    input = [int(value) for value in puzzleInput.read().split('-')]

hasDouble = re.compile(
    r'[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}')

# Find where numbers are doubles (e.g. 112345, 122456, 123345 etc).
def contains_double(number):
    return any(hasDouble.findall(str(number)))

# Returns True if the number contains a double.
def contains_exact_double(number):
    # Disallow multiples of 3-6. This works as multiplying a string gives you multiples of the string.
    disallowedMultiples = [i * str(number) for i in range(3, 6) for number in '0123456789']
    for disallowed in disallowedMultiples:
        number = str(number).replace(disallowed, '')
    return contains_double(number)

# Going from left to right, the digits never decrease; they only ever increase or stay the same.
def never_decreases(number):
    digits = [int(d) for d in str(number)]
    neverDecreases = True
    # Code is always 6 long, n-1 as this is comparing LHS with RHS.
    for i in range(5):
        if ((digits[i] <= digits[i+1]) == False):
            neverDecreases = False
            break
    return neverDecreases

# Given a range, find the number of possible combinations for part 1.
def get_possible_combinations_part_1(start, stop):
    possibleCombinations = 0
    for number in range(start, stop):
        # Two adjacent digits have to be the same.
        if (never_decreases(number) and contains_double(number)):
            possibleCombinations += 1

    return possibleCombinations

# Given a range, find the number of possible combinations for part 2.
def get_possible_combinations_part_2(start, stop):
    possibleCombinations = 0
    for number in range(start, stop):
        # The two adjacent matching digits are not part of a larger group of matching digits.
        if (never_decreases(number) and contains_exact_double(number)):
            possibleCombinations += 1

    return possibleCombinations


# Part 1.
assert contains_double(111111) == True
assert contains_double(123789) == False

assert never_decreases(111111) == True
assert never_decreases(223450) == False

print(get_possible_combinations_part_1(input[0], input[1]))

# Part 2.
assert contains_exact_double(112233) == True
assert contains_exact_double(111122) == True
assert contains_exact_double(221111) == True
assert contains_exact_double(123444) == False
assert contains_exact_double(677779) == False
assert contains_exact_double(111111) == False

print(get_possible_combinations_part_2(input[0], input[1]))
