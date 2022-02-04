# print() function works - 
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) 
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

#Output formatting 
x = 10
y = 5
print("") # most programmers refers as newline. but end='\n' is newline.
print('The value of x is {} and y is {}'.format(x,y))
#another format 
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
