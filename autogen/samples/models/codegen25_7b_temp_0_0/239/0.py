def get_total_number_of_sequences(m,n): 
  """
  Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
  """
  if n == 0:
    return 1
  elif n == 1:
    return m
  else:
    return get_total_number_of_sequences(m,n-1) + get_total_number_of_sequences(m,n-2)

def get_total_number_of_