def number_ctr(str):
  """
  Write a python function to count number of digits in a given string.
  """
  count = 0
  for i in str:
    if i.isdigit():
      count += 1
  return count

def number_ctr_2(str):
  """
  Write a python function to count number of digits in a given string.
  """
  count = 0
  for i in str:
