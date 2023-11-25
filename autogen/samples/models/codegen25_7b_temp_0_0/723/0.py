from operator import eq
def count_same_pair(nums1, nums2):
  """
  The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
  """
  count = 0
  for i in range(len(nums1)):
    if eq(nums1[i], nums2[i]):
      count += 1
  return count

def count_same_pair_2(nums1, nums2):
  """
  The input is defined as two