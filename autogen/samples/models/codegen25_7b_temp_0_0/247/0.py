def lps(str): 
  """
  Write a function to find the length of the longest palindromic subsequence in the given string.
  >>> lps("TENS FOR TENS") == 5
  """
  n = len(str)
  dp = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    dp[i][i] = 1
  for i in range(n-1, -1, -1):
    for j in range(i+1