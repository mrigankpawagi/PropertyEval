def find_lists(Input): 
  """
  Write a function to find number of lists present in the given tuple.
  """
  count = 0
  for i in Input:
    if type(i) == list:
      count += 1
  return count

print(find_lists([1, 2, [3], 4, [5, 6, [7, 8, 9]]]))

# Output: 2

# Write a function to find