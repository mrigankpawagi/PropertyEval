def first_odd(nums):
  """
  Write a python function to find the first odd number in a given list of numbers.
  >>> first_odd([1,3,5]) == 1
  """
  for num in nums:
    if num % 2 == 1:
      return num
  return None

def first_odd_recursive(nums):
  """
  Write a python function to find the first odd number in a given list of numbers.
  >>> first_odd_recursive([1,3,5])