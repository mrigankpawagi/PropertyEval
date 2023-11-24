def decimal_to_binary(n): 
  """
  Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
  >>> decimal_to_binary(8) == '1000'
  """
  return bin(n)[2:]

def binary_to_decimal(n):
  """
  Write a function to convert the given binary number to its decimal equivalent.
  >>> binary_to_decimal('101') == 5
  """
  return int(n, 2)

def decimal_to_hex(n