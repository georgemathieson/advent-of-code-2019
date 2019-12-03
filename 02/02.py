def processor(intcodes):
    for counter in range(0, len(intcodes)):

        # Each instruction is 4 long.
        if ((counter + 1) % 4 == 0):
            instructionPointer = counter - 3
            opcode = intcodes[instructionPointer]
            pos1 = intcodes[instructionPointer + 1]
            pos2 = intcodes[instructionPointer + 2]
            pos3 = intcodes[instructionPointer + 3]

            if (opcode == 1):
                intcodes[pos3] = intcodes[pos1] + intcodes[pos2]
            elif (opcode == 2):
                intcodes[pos3] = intcodes[pos1] * intcodes[pos2]
            elif (opcode == 99):
                return intcodes
            else:
                print("Something went wrong")

# Test using the given example.
example = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
actual = processor(example)
assert actual == expected

# Puzzle input.
with open('input') as puzzleInput:
    intcodes = [int(value) for value in puzzleInput.read().split(',')]

intcodes1 = intcodes.copy()

# Before running the program, replace position 1 with the value 12.
intcodes1[1] = 12

# And replace position 2 with the value 2.
intcodes1[2] = 2

# Calculate part 1.
print("part 1 answer:")
print(processor(intcodes1)[0])

# 0 to 99 inclusive.
for noun in range(0, 100):
    for verb in range(0, 100):
        # Reset computer memory.
        intcodes2 = intcodes.copy()
        intcodes2[1] = noun
        intcodes2[2] = verb
        if (processor(intcodes2)[0] == 19690720):
            print("noun:")
            print(noun)
            print("verb:")
            print(verb)

            # Calculate part 2.
            print("part 2 answer:")
            print(100 * noun + verb)
