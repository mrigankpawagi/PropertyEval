def number_of_substrings(str): 
  """
  Write a python function to count the number of non-empty substrings of a given string.
  """
  count = 0
  for i in range(len(str)):
    for j in range(i, len(str)):
      if len(str[i:j+1]) > 0:
        count += 1
  return count

def number_of_substrings_with_k_distinct_characters(