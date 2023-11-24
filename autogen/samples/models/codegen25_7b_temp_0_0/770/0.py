def odd_num_sum(n) : 
  """
  Write a python function to find the sum of fourth power of first n odd natural numbers.
  >>> odd_num_sum(2) == 82
  """
  return sum(i**4 for i in range(1, n*2, 2))

def odd_num_sum_2(n) : 
  """
  Write a python function to find the sum of fourth power of first n odd natural numbers.
  >>> odd_num_sum_2(2) == 82
 