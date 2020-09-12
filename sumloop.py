# Accept number from user and
# calculate the sum of all number between 1 and given number
sum = 0
userInput = int(input())
for number in range(1, userInput+1):
    sum += number
print(sum)
