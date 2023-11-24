def multiply_elements(test_tup):
  """
  Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
  >>> multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
  """
  return tuple(t * (t + 1) / 2 for t in test_tup[:-1])

def sum_of_squares(test_tup):
  """
  Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where