# Given a range of first 10 numbers,
# Iterate from start number to the end number and
# print the sum of the current number and previous number

previous = 0
for number in range(10):
    jog = previous+number
    print(f"Current Number {number} , Previous Number {previous} , Sum: {jog}")
    previous = number
