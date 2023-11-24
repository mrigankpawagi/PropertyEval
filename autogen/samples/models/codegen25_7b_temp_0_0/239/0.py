def get_total_number_of_sequences(m,n): 
  """
  Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
  >>> get_total_number_of_sequences(10, 4) == 4
  """
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 3
  else:
    return get_total_number_of_sequences(m, n-1) + get_total_number_of_sequences(m, n-2