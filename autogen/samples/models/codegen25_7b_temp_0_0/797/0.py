def sum_odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_range(l,r): 
  """
  Write a python function to find the sum of all odd natural numbers within the range l and r.
  """
  sum = 0
  for i in range(l,r+1):
    if i%2 != 0:
      sum += i
  return sum
def sum_even(n): 
    terms = n//2
    sum1 = terms * (terms + 1) 
    return sum1  
def sum_in