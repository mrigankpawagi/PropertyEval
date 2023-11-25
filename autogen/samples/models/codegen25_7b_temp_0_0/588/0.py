def big_diff(nums):
  """
  Write a python function to find the difference between largest and smallest value in a given list.
  """
  return max(nums) - min(nums)

def centered_average(nums):
  """
  Write a python function to find the average of the values in a list, except ignoring the largest and smallest values in the list.
  """
  nums.sort()
  return sum(nums[1:-1