def remove_odd(str1):
  """
  Write a function to remove odd characters in a string.
  """
  return ''.join(filter(lambda x: x % 2 == 0, str1))

print(remove_odd('abcdefg'))

def remove_odd2(str1):
  """
  Write a function to remove odd characters in a string.
  """
  return ''.join(filter(lambda x: