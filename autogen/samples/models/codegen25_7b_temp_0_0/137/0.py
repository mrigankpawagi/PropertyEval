from array import array
def zero_count(nums):
  """
  Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
  """
  zeros = 0
  non_zeros = 0
  for i in nums:
    if i == 0:
      zeros += 1
    else:
      non_zeros += 1
  return zeros / non_zeros

def find_duplicates(nums):
  """
  Write a