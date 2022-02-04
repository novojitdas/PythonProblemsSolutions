# Write a function calculation() such that it can accept two variables
# and calculate the addition and subtraction of it.
# And also it must return both addition and subtraction in a single return call

def calculation(inputa, inputb):
    addition = inputa + inputb
    if inputa > inputb:
        subtraction = inputa - inputb
    else:
        subtraction = inputb - inputa
    return addition, subtraction


print("start")
result = calculation(50, 20)
print(result)
