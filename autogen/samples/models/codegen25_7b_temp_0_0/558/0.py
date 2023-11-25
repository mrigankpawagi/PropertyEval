def digit_distance_nums(n1, n2):
  """
  Write a python function to find the sum of the per-digit difference between two integers.
  """
  n1_str = str(n1)
  n2_str = str(n2)
  n1_list = list(n1_str)
  n2_list = list(n2_str)
  n1_list = [int(i) for i in n1_list]
  n2