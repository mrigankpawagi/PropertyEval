from collections import defaultdict
def max_occurrences(nums):
  """
  Write a function to find the item with maximum frequency in a given list.
  """
  # Time O(n) || Space O(n)
  if len(nums) == 0:
    return None
  max_count = 0
  max_item = None
  count = defaultdict(int)
  for num in nums:
    count[num] += 1
    if count[num] >