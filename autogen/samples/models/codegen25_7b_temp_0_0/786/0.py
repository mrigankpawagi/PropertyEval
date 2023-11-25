import bisect
def right_insertion(a, x):
  """
  Write a function to locate the right insertion point for a specified value in sorted order.
  """
  i = bisect.bisect_right(a, x)
  if i != len(a):
    return i
  else:
    return -1

def left_insertion(a, x):
  """
  Write a function to locate the left insertion point for a specified value in sorted order.
  """
