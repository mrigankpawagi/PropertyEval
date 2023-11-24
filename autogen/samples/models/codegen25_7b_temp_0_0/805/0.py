def max_sum_list(lists):
  """
  Write a function that returns the list in a list of lists whose sum of elements is the highest.
  >>> max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
  """
  return max(lists, key=sum)

def max_sum_list_2(lists):
  """
  Write a function that returns the list in a list of lists whose sum of elements is the highest.
  >>> max_sum_list_2([[1,2,3], [4,5,6], [10