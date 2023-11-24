from collections import defaultdict
def max_occurrences(nums):
  """
  Write a function to find the item with maximum frequency in a given list.
  >>> max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
  """
  d = defaultdict(int)
  for i in nums:
    d[i] += 1
  return max(d.values())

def max_occurrences_2(nums):
  """
  Write a function to find the item with maximum frequency in a given list.
  >>> max_occurrences