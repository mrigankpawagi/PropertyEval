def max_of_nth(test_list, N):
  """
  Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
  """
  return max([test_list[i][N-1] for i in range(len(test_list))])

def max_of_nth_2(test_list, N):
  """
  Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
  """