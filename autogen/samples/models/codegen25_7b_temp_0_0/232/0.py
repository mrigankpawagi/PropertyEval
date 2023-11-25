import heapq
def larg_nnum(list1,n):
  """
  Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
  """
  largest_nums = []
  for i in range(n):
    largest_nums.append(max(list1))
    list1.remove(max(list1))
  return largest_nums

def smallest_nnum(list1,n):
  """
  Write a function that takes in a list