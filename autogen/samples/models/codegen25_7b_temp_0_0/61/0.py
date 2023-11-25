from collections import defaultdict
def count_Substrings(s):
  """
  Write a python function to count the number of substrings with the sum of digits equal to their length.
  """
  count = 0
  for i in range(len(s)):
    for j in range(i, len(s)):
      if sum(map(int, list(s[i:j+1]))) == j-i+1:
        count += 1
  return count

def count_Substrings_2