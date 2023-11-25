def count_X(tup, x): 
  """
  Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
  """
  count = 0
  for i in tup:
    if i == x:
      count += 1
  return count

def count_X_recursive(tup, x):
  """
  Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
