def big_sum(nums):
  """
  Write a python function to find the sum of the largest and smallest value in a given array.
  """
  return max(nums) + min(nums)

def count_evens(nums):
  """
  Write a python function to count the number of even numbers in a given array.
  """
  return len([x for x in nums if x % 2 == 0])

def big_diff(nums