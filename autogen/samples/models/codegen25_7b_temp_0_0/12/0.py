def sort_matrix(M):
  """
  Write a function to sort a given matrix in ascending order according to the sum of its rows.
  """
  M.sort(key=lambda x: sum(x))
  return M

def sort_matrix_2(M):
  """
  Write a function to sort a given matrix in ascending order according to the sum of its rows.
  """
  M.sort(key=lambda x: sum(x))
  return