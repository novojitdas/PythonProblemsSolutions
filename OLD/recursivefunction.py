# Write a recursive function
# to calculate the sum of numbers from 0 to 10

def recurs(num):
    if num:
        return num + recurs(num-1)
    else:
        return 0


print("start")
res = recurs(3)
print(res)
