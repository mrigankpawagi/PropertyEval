def sum_digits(n):
  """
  Write a function to get the sum of the digits of a non-negative integer.
  >>> sum_digits(345)==12
  """
  sum = 0
  while n > 0:
    sum += n % 10
    n = n // 10
  return sum

def sum_digits_recursive(n):
  """
  Write a function to get the sum of the digits of a non-negative integer.
  >>> sum_digits_recursive(