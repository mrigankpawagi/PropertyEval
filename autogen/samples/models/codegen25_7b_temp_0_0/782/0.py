def odd_length_sum(arr):
  """
  Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
  """
  sum = 0
  for i in range(len(arr)):
    for j in range(i, len(arr), 2):
      sum += arr[j]
  return sum

def odd_length_sum_2(arr):
  """
  Write a python function to find the sum of all odd length subarr