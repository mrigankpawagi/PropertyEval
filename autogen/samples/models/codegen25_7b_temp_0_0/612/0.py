def merge(lst):  
  """
  Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
  >>> merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
  """
  return [[lst[i][0] for i in range(len(lst))], [lst[i][1] for i in range(len(lst))]]

def merge_sort(lst):
  """
  Write a python function which takes a list of integers and returns a sorted list of integers.
 