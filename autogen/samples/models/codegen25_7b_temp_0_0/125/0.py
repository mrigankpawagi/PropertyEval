def find_length(string): 
  """
  Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
  >>> find_length("11000010001") == 6
  """
  # Fill this in.
  max_length = 0
  for i in range(len(string)):
    for j in range(i, len(string)):
      if string[j] == '0':
        max_length = max(max_length, j - i + 1)
      else:
        max