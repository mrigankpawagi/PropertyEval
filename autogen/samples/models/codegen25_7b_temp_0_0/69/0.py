def is_sublist(l, s):
  """
  Write a function to check whether a list contains the given sublist or not.
  >>> is_sublist([2,4,3,5,7],[3,7])==False
  """
  if len(l) < len(s):
    return False
  for i in range(len(l) - len(s) + 1):
    if l[i:i + len(s)] == s:
      return True
  return False


def is_sublist_recursive(l, s):
 