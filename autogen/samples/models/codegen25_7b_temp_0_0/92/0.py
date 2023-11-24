def is_undulating(n): 
  """
  Write a function to check whether the given number is undulating or not.
  >>> is_undulating(1212121) == True
  """
  if n < 10:
    return False
  else:
    n = str(n)
    for i in range(1, len(n)):
      if n[i] == n[i-1]:
        return False
      elif n[i] > n[i-1]:
        return True
     