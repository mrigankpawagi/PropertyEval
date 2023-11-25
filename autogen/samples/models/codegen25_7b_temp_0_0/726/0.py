def multiply_elements(test_tup):
  """
  Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
  """
  return tuple(test_tup[i] * test_tup[i+1] for i in range(len(test_tup)-1))

def sum_elements(test_tup):
  """
  Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1