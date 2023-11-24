from array import array
def positive_count(nums):
  """
  Write a function to find the ration of positive numbers in an array of integers.
  >>> positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
  """
  count = 0
  for i in nums:
    if i > 0:
      count += 1
  return count/len(nums)

def reverse_array(nums):
  """
  Write a function to reverse an array of integers.
  >>> reverse_array([1, 2, 3, 4, 5