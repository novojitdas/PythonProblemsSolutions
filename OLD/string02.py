# Given 2 strings, s1 and s2,
# create a new string by appending s2 in the middle of s1

def mid(s1, s2):
    middleIndex = int(len(s1)/2)
    print("The First String: ", s1)
    finalStr = s1[:middleIndex:] + s2 + s1[middleIndex:]
    print("The Final String Is: ", finalStr)


print("Start")
mid("RobDam", "Van")
