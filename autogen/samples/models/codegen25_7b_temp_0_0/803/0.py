def is_perfect_square(n) :
  """
  Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
  >>> not is_perfect_square(10)
  """
  if (n == 0) : 
    return True
  if (n <= 3) : 
    return False
  i = 1
  while (i * i <= n) : 
    if (i * i == n) : 
      return True
    i += 1
  return False

def is_perfect