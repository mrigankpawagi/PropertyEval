def pancake_sort(nums):
  """
  Write a function to sort a list of elements.
  >>> pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
  """
  for i in range(len(nums)):
    max_index = nums.index(max(nums[:i+1]))
    if max_index != i:
      nums[:i+1] = nums[:i+1][::-1]
      nums[:max_index