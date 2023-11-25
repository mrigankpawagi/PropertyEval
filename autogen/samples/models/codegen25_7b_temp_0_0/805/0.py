def max_sum_list(lists):
  """
  Write a function that returns the list in a list of lists whose sum of elements is the highest.
  """
  max_sum = 0
  max_list = []
  for list in lists:
    sum = 0
    for i in list:
      sum += i
    if sum > max_sum:
      max_sum = sum
      max_list = list
  return max_list

print(max_sum_list