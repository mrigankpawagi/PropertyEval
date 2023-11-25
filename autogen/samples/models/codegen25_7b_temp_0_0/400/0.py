def extract_freq(test_list):
  """
  Write a function to extract the number of unique tuples in the given list.
  """
  freq = {}
  for i in test_list:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1
  return len(freq)

def extract_freq_2(test_list):
  """
  Write a function to