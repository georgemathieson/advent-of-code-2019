import re

# Puzzle input.
with open('input') as puzzleInput:
    input = [int(value) for value in puzzleInput.read().split('-')]

# Regex for part 1.
hasDouble = re.compile(
    r'[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}')

# Given a range, find the number of possible combinations for part 1.
def get_possible_combinations_part_1(start, stop):
    possibleCombinations = 0
    for number in range(start, stop):
        # Two adjacent digits have to be the same.
        if (any(hasDouble.findall(str(number)))):
            if (never_decreases(number)):
                possibleCombinations += 1

    return possibleCombinations

# Given a range, find the number of possible combinations for part 2.
def get_possible_combinations_part_2(start, stop):
    possibleCombinations = 0
    for number in range(start, stop):
        # The two adjacent matching digits are not part of a larger group of matching digits.
        if (contains_exact_double(number)):
            if (never_decreases(number)):
                possibleCombinations += 1

    return possibleCombinations

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

# Returns True if the number contains a double.
def contains_exact_double(number):
    containsExactDouble = False
    digits = [int(d) for d in str(number)]
    for i in range(5):
        if (digits[i] == digits[i+1]):
            if (i == 0 and digits[i] != digits[i+2]):
                containsExactDouble = True
                break
            elif (i == 4 and digits[i] != digits[i-1]):
                containsExactDouble = True
                break
            elif (digits[i] != digits[i-1] and digits[i] != digits[i+2]):
                containsExactDouble = True
                break

    return containsExactDouble


# Part 1.
print(get_possible_combinations_part_1(input[0], input[1]))

# Part 2.
assert contains_exact_double(112233) == True
assert contains_exact_double(111122) == True
assert contains_exact_double(221111) == True
assert contains_exact_double(123444) == False
assert contains_exact_double(677779) == False
assert contains_exact_double(111111) == False

print(get_possible_combinations_part_2(input[0], input[1]))
