def largest_subset(a):
  """
  Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
  >>> largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
  """
  # Sort the list
  a.sort()
  # Initialize the largest subset
  largest_subset = []
  # Initialize the current subset
  current_subset = []
  # Initialize the current sum
  current_sum = 0
  # Iterate through the list
  for i in range(len(