def sum_even_and_even_index(arr):  
  """
  Write a python function to find the sum of even numbers at even positions of a list.
  >>> sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
  """
  sum = 0
  for i in range(0, len(arr), 2):
    if arr[i] % 2 == 0:
      sum += arr[i]
  return sum

def sum_even_and_even_index_2(arr):  
  """
  Write a python function to find the sum of