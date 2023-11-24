def odd_length_sum(arr):
  """
  Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
  >>> odd_length_sum([1,2,4]) == 14
  """
  return sum([sum(arr[i:i+j]) for i in range(len(arr)) for j in range(1, len(arr)-i+1, 2)])

def odd_length_sum_2(arr):
  """
  Write a python function to find the sum of all odd length subarrays.