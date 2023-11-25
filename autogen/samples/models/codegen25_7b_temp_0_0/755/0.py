def second_smallest(numbers):
  """
  Write a function to find the second smallest number in a list.
  """
  numbers.sort()
  return numbers[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))
# -2

print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# -2

print(