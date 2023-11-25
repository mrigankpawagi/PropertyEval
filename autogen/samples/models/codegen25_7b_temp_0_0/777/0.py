def find_sum(arr): 
  """
  Write a python function to find the sum of non-repeated elements in a given list.
  """
  sum = 0
  for i in arr:
    if arr.count(i) == 1:
      sum += i
  return sum

print(find_sum([1,2,3,4,5,6,7,8,9,10]))

def find_sum_2(arr):
  """