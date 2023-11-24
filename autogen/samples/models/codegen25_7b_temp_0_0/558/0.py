def digit_distance_nums(n1, n2):
  """
  Write a python function to find the sum of the per-digit difference between two integers.
  >>> digit_distance_nums(1,2) == 1
  """
  return sum(abs(int(i) - int(j)) for i, j in zip(str(n1), str(n2)))

def digit_distance_nums_2(n1, n2):
  """
  Write a python function to find the sum of the per-digit difference between two integers.
 