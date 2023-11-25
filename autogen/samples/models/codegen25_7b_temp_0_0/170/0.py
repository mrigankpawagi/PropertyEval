def sum_range_list(list1, m, n):                                                                                                                                                                                                
  """
  Write a function to find the sum of numbers in a list within a range specified by two indices.
  """
  sum = 0
  for i in range(m, n+1):
    sum += list1[i]
  return sum

def sum_range_list_2(list1, m, n):
  """
  Write a function to find the sum of numbers in a list within a range specified by two indices.
 