def sum_list(lst1,lst2):
  """
  Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
  >>> sum_list([10,20,30],[15,25,35])==[25,45,65]
  """
  return [a+b for a,b in zip(lst1,lst2)]

def sum_list_recursive(lst1,lst2):
  """
  Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [