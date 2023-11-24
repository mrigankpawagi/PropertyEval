def count_no_of_ways(n, k): 
  """
  Write a function to find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color for the given fence with n posts and k colors.
  >>> count_no_of_ways(2, 4) == 16
  """
  if n == 0: 
    return 0
  if n == 1: 
    return k
  if k == 0: 
    return 0
  if k == 1: 
    return 1
  return count_no_of_ways(n-1, k) + count_no_of_ways(n-