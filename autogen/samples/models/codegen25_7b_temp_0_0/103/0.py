def eulerian_num(n, m): 
  """
  Write a function to find the Eulerian number a(n, m).
  """
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n == 2:
    return m
  if n == 3:
    return m * (m + 1) // 2
  if n == 4:
    return m * (m + 1) * (m + 2) //