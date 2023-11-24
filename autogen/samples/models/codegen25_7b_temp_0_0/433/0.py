def check_greater(arr, number):
  """
  Write a function to check whether the entered number is greater than the elements of the given array.
  >>> check_greater([1, 2, 3, 4, 5], 4) == False
  """
  for i in arr:
    if i > number:
      return True
  return False

def check_greater_equal(arr, number):
  """
  Write a function to check whether the entered number is greater than or equal to the elements of the given array.
  >>> check_greater_equal([1, 2