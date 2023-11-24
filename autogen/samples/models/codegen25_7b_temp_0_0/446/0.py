from collections import Counter 
def count_Occurrence(tup, lst): 
  """
  Write a python function to count the occurence of all elements of list in a tuple.
  >>> count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
  """
  return sum(1 for i in lst if i in tup) 

def count_Occurrence_dict(tup, lst): 
  """
  Write a python function to count the occurence of all elements of list in a tuple.
  >>> count_Occurrence_dict(('a', 'a', '