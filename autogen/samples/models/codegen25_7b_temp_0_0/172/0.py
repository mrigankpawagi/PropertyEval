def count_occurance(s):
  """
  Write a function to count the number of occurence of the string 'std' in a given string.
  """
  count = 0
  for i in range(len(s)-2):
    if s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd':
      count += 1
  return count

def count_occurance_2(s):
  """
