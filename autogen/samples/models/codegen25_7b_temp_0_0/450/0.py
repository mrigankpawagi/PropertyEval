def extract_string(str, l):
  """
  Write a function to extract specified size of strings from a given list of string values.
  """
  return [str[i:i+l] for i in range(0, len(str), l)]

def extract_string_2(str, l):
  """
  Write a function to extract specified size of strings from a given list of string values.
  """
  return [str[i:i+l] for