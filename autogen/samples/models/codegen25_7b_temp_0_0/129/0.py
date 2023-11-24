def magic_square_test(my_matrix):
  """
  Write a function to calculate whether the matrix is a magic square.
  >>> magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
  """
  # check if the matrix is square
  if len(my_matrix) != len(my_matrix[0]):
    return False
  # check if the matrix is magic
  if sum(my_matrix[0]) == sum(my_matrix[i][0] for i in range(1, len(