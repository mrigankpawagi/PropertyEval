def count(lst):   
  """
  Write a python function to count true booleans in the given list.
  """
  return sum(lst)

print(count([True, False, True, True, False]))

def count_strings(lst):
  """
  Write a python function to count strings in the given list.
  """
  return sum(isinstance(x, str) for x in lst)

print