# Given a string of odd length greater 7,
# return a string made of the middle three chars of a given String

def getMiddleThreeChars(sample):
    middleIndex = int(len(sample)/2)
    print("Original String Is: ", sample)
    middleThree = sample[middleIndex-1:middleIndex+2]
    print("Middle 3 is: ", middleThree)


print("Start")
getMiddleThreeChars("jaSonja")
getMiddleThreeChars("RobVanDam")
