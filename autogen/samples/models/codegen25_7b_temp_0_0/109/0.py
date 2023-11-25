def odd_Equivalent(s,n): 
  """
  Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
  """
  count = 0
  for i in range(n):
    s = s[1:] + s[0]
    count += s.count('1')
  return count

def odd_Equivalent(s,n): 
  """
  Write a python function to find the number of numbers with an odd value when rotating a