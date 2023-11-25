from array import array
def positive_count(nums):
  """
  Write a function to find the ration of positive numbers in an array of integers.
  """
  count = 0
  for num in nums:
    if num > 0:
      count += 1
  return count / len(nums)

def positive_count_2(nums):
  """
  Write a function to find the ration of positive numbers in an array of integers.
  """
  return sum(