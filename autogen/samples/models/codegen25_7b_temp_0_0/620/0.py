def largest_subset(a):
  """
  Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
  """
  # Time O(n) || Space O(n)
  if len(a) < 2:
    return a

  a.sort()
  largest_subset = [a[0]]
  for i in range(1, len(a)):
    if a[i] % a[i - 1] == 0