# Given 2 strings, s1, and s2 return a
# new string made of the first, middle and last char each input string

def string(s1, s2):
    print("First String Is: ", s1)
    midIndex = int(len(s1)/2)
    midIndex2 = int(len(s2)/2)
    first_char = s1[:1]+s2[:1]
    middle_char = s1[midIndex:midIndex+1] + s2[midIndex2:midIndex2+1]
    last_char = s1[len(s1)-1] + s2[len(s2)-1]
    final = first_char + middle_char + last_char
    print("Output will be :", final)


print("Start")
string("America", "Japan")
