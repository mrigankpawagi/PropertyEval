def sum_range_list(list1, m, n):                                                                                                                                                                                                
  """
  Write a function to find the sum of numbers in a list within a range specified by two indices.
  >>> sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
  """
  sum = 0
  for i in range(m, n+1):
    sum += list1[i]
  return sum

def sum_range_list_2(list1, m, n):                                                                                                                                                                                                
  """
  Write a function to find the sum of numbers in a list within a range