from array import array
def zero_count(nums):
  """
  Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
  >>> math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
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