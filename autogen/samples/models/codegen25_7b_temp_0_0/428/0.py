def shell_sort(my_list):
  """
  Write a function to sort the given array by using shell sort.
  >>> shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
  """
  gap = len(my_list) // 2
  while gap > 0:
    for i in range(gap, len(my_list)):
      temp = my_list[i]
      j = i
      while j >= gap and my_list[j - gap] > temp:
        my_list[j]