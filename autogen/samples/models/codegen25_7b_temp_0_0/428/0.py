def shell_sort(my_list):
  """
  Write a function to sort the given array by using shell sort.
  """
  gap = len(my_list) // 2
  while gap > 0:
    for i in range(gap, len(my_list)):
      temp = my_list[i]
      j = i
      while j >= gap and my_list[j - gap] > temp:
        my_list[j]