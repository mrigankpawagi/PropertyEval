def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def get_coordinates(test_tup):
  """
  Write a function to extract all the adjacent coordinates of the given coordinate tuple.
  """
  return list(adjac(test_tup))

print(get_coordinates((1,2)))

#%%
"""
Write a function to find the minimum number of steps required to reach the end of the maze from the start.
"""
def find_path(maze):
  """
  Write a function to find