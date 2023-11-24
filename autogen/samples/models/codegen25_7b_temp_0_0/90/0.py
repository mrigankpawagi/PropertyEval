def len_log(list1):
  """
  Write a python function to find the length of the longest word.
  >>> len_log(["python","PHP","bigdata"]) == 7
  """
  return max(len(word) for word in list1)

def len_log_2(list1):
  """
  Write a python function to find the length of the longest word.
  >>> len_log_2(["python","PHP","bigdata"]) == 7
  """
  return max(map(