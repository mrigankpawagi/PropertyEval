def pancake_sort(nums):
  """
  Write a function to sort a list of elements.
  """
  for i in range(len(nums), 1, -1):
    max_index = nums.index(max(nums[:i]))
    if max_index != i - 1:
      nums[:i] = nums[:i][::-1]
      nums[:max_index