def max_of_nth(test_list, N):
  """
  Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
  >>> max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
  """
  return max(row[N] for row in test_list)

def max_of_nth_2(test_list, N):
  """
  Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
  >>> max_of_nth_2([[5