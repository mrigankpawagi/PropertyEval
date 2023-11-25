def find_length(string): 
  """
  Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
  """
  # Time O(n) || Space O(1)
  max_length = 0
  ones = 0
  zeros = 0
  for char in string:
    if char == '0':
      zeros += 1
    else:
      ones += 1
    max_length = max(max_length, abs(