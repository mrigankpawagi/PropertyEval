def check_greater(arr, number):
  """
  Write a function to check whether the entered number is greater than the elements of the given array.
  """
  for i in arr:
    if i > number:
      return True
  return False

def check_greater_recursive(arr, number):
  """
  Write a function to check whether the entered number is greater than the elements of the given array.
  """
  if len(arr) == 0:
   