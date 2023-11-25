def pos_count(list):
  """
  Write a python function to count the number of positive numbers in a list.
  """
  count = 0
  for i in list:
    if i > 0:
      count += 1
  return count

def neg_count(list):
  """
  Write a python function to count the number of negative numbers in a list.
  """
  count = 0
  for i in list:
    if i