import collections
def freq_count(list1):
  """
  Write a function to get the frequency of all the elements in a list, returned as a dictionary.
  >>> freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
  """
  freq = {}
  for i in list1:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1
  return freq

def remove_duplicates(list1):
  """
  Write a function to remove duplicates from a list