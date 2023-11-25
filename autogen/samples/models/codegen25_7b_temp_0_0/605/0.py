def prime_num(num):
  """
  Write a function to check if the given integer is a prime number.
  """
  if num == 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def prime_num_2(num):
  """
  Write a function to check if the given integer is a prime number.
  """
  if num