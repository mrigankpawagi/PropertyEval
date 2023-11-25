def frequency(a,x): 
  """
  Write a function to count the number of occurrences of a number in a given list.
  """
  count = 0
  for i in a:
    if i == x:
      count += 1
  return count

def reverse(a):
  """
  Write a function to reverse a list.
  """
  return a[::-1]

def sort(a):
  """
  Write a function to