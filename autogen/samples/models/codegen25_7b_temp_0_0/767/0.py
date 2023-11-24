def get_pairs_count(arr, sum):
  """
  Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
  >>> get_pairs_count([1,1,1,1],2) == 6
  """
  count = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == sum:
        count += 1
  return count

def get_pairs_count_with_dict(arr, sum):
