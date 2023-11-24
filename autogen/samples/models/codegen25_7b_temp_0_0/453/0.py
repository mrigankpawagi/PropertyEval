import math 
def sumofFactors(n) : 
  """
  Write a python function to find the sum of even factors of a number.
  >>> sumofFactors(18) == 26
  """
  sum = 0
  for i in range(1, int(math.sqrt(n)) + 1) : 
    if (n % i == 0) : 
      if (i % 2 == 0) : 
        sum += i 
        if (n // i != i) : 
          sum += n //