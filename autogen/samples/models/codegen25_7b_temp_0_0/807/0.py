def first_odd(nums):
  """
  Write a python function to find the first odd number in a given list of numbers.
  """
  for num in nums:
    if num % 2 != 0:
      return num
  return None

def first_odd_recursive(nums):
  """
  Write a python function to find the first odd number in a given list of numbers.
  """
  if len(nums) == 0:
   