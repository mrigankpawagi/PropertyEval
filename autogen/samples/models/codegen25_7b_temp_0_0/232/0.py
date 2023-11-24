import heapq
def larg_nnum(list1,n):
  """
  Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
  >>> set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
  """
  return heapq.nlargest(n,list1)

def larg_nnum_2(list1,n):
  """
  Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
  >>> set(larg_nnum_2([10, 20, 50