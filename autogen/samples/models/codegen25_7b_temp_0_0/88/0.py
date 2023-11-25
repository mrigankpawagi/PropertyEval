import collections
def freq_count(list1):
  """
  Write a function to get the frequency of all the elements in a list, returned as a dictionary.
  """
  freq = {}
  for i in list1:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1
  return freq

def freq_count_2(list1):
  """
  Write a function to get the frequency of all