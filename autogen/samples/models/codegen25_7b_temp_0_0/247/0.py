def lps(str): 
  """
  Write a function to find the length of the longest palindromic subsequence in the given string.
  """
  n = len(str) 
  L = [[0 for x in range(n)] for x in range(n)] 
  for i in range(n): 
    L[i][i] = 1
  for cl in range(2, n+1): 
    for i in range(n-cl+1