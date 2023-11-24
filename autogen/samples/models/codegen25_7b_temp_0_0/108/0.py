import heapq
def merge_sorted_list(num1,num2,num3):
  """
  Write a function to merge three lists into a single sorted list.
  >>> merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
  """
  num1.extend(num2)
  num1.extend(num3)
  num1.sort()
  return num1

def merge_sorted_list_2(num1,num2,num3):
  """
  Write a function to merge three lists into a single sorted list.
  >>>