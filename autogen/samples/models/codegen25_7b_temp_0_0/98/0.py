def multiply_num(numbers):  
  """
  Write a function to multiply all the numbers in a list and divide with the length of the list.
  """
  total = 1
  for number in numbers:
    total *= number
  return total / len(numbers)

print(multiply_num([1,2,3,4,5]))

# Write a function to find the smallest number in a list.
def smallest_num(numbers):
  """