# Given a two integer numbers return their product and  if
# the product is greater than 1000, then return their sum
#

number1 = int(input(""))
number2 = int(input(""))
product = number1 * number2
if product < 1000:
    print(product)
else:
    print(number1+number2)
