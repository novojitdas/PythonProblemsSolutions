# Arrange string characters such that
# lowercase letters should come first

str1 = "PyThon"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = "" .join(lower+upper)
print(sorted_string)
