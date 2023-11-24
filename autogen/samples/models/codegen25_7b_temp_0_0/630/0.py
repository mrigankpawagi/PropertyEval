def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def get_coordinates(test_tup):
  """
  Write a function to extract all the adjacent coordinates of the given coordinate tuple.
  >>> get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
  """
  return list(adjac(test_tup))

def get_neighbors(test_tup):
  """
  Write a function to extract all the neighbors of the given coordinate tuple.
  >>> get_neighbors((3, 4)) == [[2, 3], [2, 4], [2, 5], [