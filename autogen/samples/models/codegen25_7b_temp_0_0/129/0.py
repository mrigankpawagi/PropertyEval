def magic_square_test(my_matrix):
  """
  Write a function to calculate whether the matrix is a magic square.
  """
  # Check if the matrix is a square
  if len(my_matrix) != len(my_matrix[0]):
    return False

  # Check if the matrix is a magic square
  # Get the sum of each row and column
  row_sums = [sum(row) for row in my_matrix