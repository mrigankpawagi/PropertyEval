def decimal_to_binary(n): 
  """
  Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
  """
  if n == 0:
    return '0'
  binary = ''
  while n > 0:
    binary += str(n % 2)
    n = n // 2
  return binary[::-1]

def binary_to_decimal(binary):
  """
  Write a function to convert the given binary