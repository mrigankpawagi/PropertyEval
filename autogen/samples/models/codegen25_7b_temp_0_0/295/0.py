def sum_div(number):
  """
  Write a function to return the sum of all divisors of a number.
  >>> sum_div(8)==7
  """
  sum = 0
  for i in range(1, number):
    if number % i == 0:
      sum += i
  return sum

def sum_div_2(number):
  """
  Write a function to return the sum of all divisors of a number.
  >>> sum_div_2(8