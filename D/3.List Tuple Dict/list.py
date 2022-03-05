# Python: Sum all the items in a list
def sum_list(items):
      sum_numbers = 0
      for i in items:
            sum_numbers = sum_numbers+i
      return sum_numbers


print(sum_list([1,2,3]))
print(sum_list([10,20,30]))