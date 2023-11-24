def sum_odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_range(l,r): 
  """
  Write a python function to find the sum of all odd natural numbers within the range l and r.
  >>> sum_in_range(2,5) == 8
  """
  return sum_odd(r) - sum_odd(l - 1)

def sum_in_range_2(l,r):
  """
  Write a python function to find the sum of all odd natural numbers within the range l and r.
  >>> sum_in_range_2(2,5) == 8
