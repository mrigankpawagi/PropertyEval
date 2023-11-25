def max_difference(test_list):
  """
  Write a function to find the maximum difference between available pairs in the given tuple list.
  """
  test_list.sort()
  max_diff = 0
  for i in range(len(test_list) - 1):
    diff = test_list[i + 1] - test_list[i]
    if diff > max_diff:
      max_diff = diff
  return max_diff

print(