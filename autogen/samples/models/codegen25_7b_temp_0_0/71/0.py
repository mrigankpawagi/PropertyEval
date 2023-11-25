def comb_sort(nums):
  """
  Write a function to sort a list of elements.
  """
  gap = len(nums)
  swapped = True
  while gap > 1 or swapped:
    gap = max(1, int(gap / 1.25))
    swapped = False
    for i in range(len(nums) - gap):
      if nums[i] > nums[i + gap]:
