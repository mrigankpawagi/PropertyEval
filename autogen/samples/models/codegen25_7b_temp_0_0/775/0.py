def odd_position(nums):
  """
  Write a python function to check whether every odd index contains odd numbers of a given list.
  >>> odd_position([2,1,4,3,6,7,6,3]) == True
  """
  for i in range(1, len(nums), 2):
    if nums[i] % 2 == 0:
      return False
  return True

def odd_position_2(nums):
  """
  Write a python function to check whether every odd index contains odd numbers of a given list.
  >>> odd