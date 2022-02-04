# Print the following pattern

lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row+1):
        # end=" " is for space, only comma will new line
        print(column, end=" ")
    print(" ")  # print with black string means newline
