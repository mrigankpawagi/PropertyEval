def closest_num(N):
  """
  Write a function to find the closest smaller number than n.
  """
  if N == 1:
    return -1
  for i in range(N-1, 0, -1):
    if i < N and i > 0:
      if i % 2 == 0:
        if i % 3 == 0:
          if i % 5 == 0:
            return i
        else:
         