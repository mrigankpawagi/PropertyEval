import heapq
def merge_sorted_list(num1,num2,num3):
  """
  Write a function to merge three lists into a single sorted list.
  """
  num1.extend(num2)
  num1.extend(num3)
  num1.sort()
  return num1

def merge_sorted_list_2(num1,num2,num3):
  """
  Write a function to merge three lists into a single sorted list.
  """