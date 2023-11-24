def cube_nums(nums):
  """
  Write a function to find cubes of individual elements in a list.
  >>> cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
  """
  return [num**3 for num in nums]

def cube_nums_map(nums):
  """
  Write a function to find cubes of individual elements in a list.
  >>> cube_nums_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[