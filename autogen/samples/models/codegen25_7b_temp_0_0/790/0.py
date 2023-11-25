def even_position(nums):
  """
  Write a python function to check whether every even index contains even numbers of a given list.
  """
  for i in range(0, len(nums), 2):
    if nums[i] % 2 != 0:
      return False
  return True

def odd_position(nums):
  """
  Write a python function to check whether every odd index contains odd numbers of a given list.
  """
  for