def two_unique_nums(nums):
  """
  Write a python function to remove duplicate numbers from a given number of lists.
  """
  unique_nums = []
  for num in nums:
    if num not in unique_nums:
      unique_nums.append(num)
  return unique_nums

def two_unique_nums_2(nums):
  """
  Write a python function to remove duplicate numbers from a given