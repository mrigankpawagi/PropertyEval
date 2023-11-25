def count_list(input_list): 
  """
  Write a python function to count the number of lists in a given number of lists.
  """
  count = 0
  for i in input_list:
    if type(i) == list:
      count += 1
  return count

def count_tuple(input_tuple): 
  """
  Write a python function to count the number of tuples in a given number of tuples.
  """
 