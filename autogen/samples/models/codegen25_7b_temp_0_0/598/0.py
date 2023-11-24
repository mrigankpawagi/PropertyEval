def armstrong_number(number):
  """
  Write a function to check whether the given number is armstrong or not.
  >>> armstrong_number(153)==True
  """
  sum = 0
  temp = number
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  return sum == number

def armstrong_number_2(number):
  """
  Write a function to check whether the given number is armstrong or not.
