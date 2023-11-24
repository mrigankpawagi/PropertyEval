import bisect
def right_insertion(a, x):
  """
  Write a function to locate the right insertion point for a specified value in sorted order.
  >>> right_insertion([1,2,4,5],6)==4
  """
  i = bisect.bisect_right(a, x)
  if i == len(a):
    return i - 1
  return i

def left_insertion(a, x):
  """
  Write a function to locate the left insertion point for a specified value in sorted order.
  >>> left_insertion