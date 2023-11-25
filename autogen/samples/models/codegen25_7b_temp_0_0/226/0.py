def odd_values_string(str):
  """
  Write a python function to remove the characters which have odd index values of a given string.
  """
  return ''.join(str[i] for i in range(len(str)) if i % 2 == 0)

print(odd_values_string("Python"))

def odd_values_string(str):
  """
  Write a python function to remove the characters which have odd index values of a given string.
  """