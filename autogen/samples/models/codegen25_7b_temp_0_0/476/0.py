def big_sum(nums):
  """
  Write a python function to find the sum of the largest and smallest value in a given array.
  >>> big_sum([1,2,3]) == 4
  """
  return max(nums) + min(nums)

def count_evens(nums):
  """
  Write a python function to count the number of even numbers in a given array.
  >>> count_evens([2,1,2,3,4]) == 3
  """
  return sum(1 for