import bisect
def left_insertion(a, x):
  """
  Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
  >>> left_insertion([1,2,4,5],6)==4
  """
  i = bisect.bisect_left(a, x)
  if i != len(a) and a[i] == x:
    return i
  return i

def right_insertion(a, x):
  """
  Write a function to locate the right insertion point for a specified value in sorted order. https