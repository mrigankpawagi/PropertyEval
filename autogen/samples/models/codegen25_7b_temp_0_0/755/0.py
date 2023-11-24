def second_smallest(numbers):
  """
  Write a function to find the second smallest number in a list.
  >>> second_smallest([1, 2, -8, -2, 0, -2])==-2
  """
  numbers.sort()
  return numbers[1]

def second_largest(numbers):
  """
  Write a function to find the second largest number in a list.
  >>> second_largest([1, 2, -8, -2, 0, -2])==0
  """
  numbers.sort()
 