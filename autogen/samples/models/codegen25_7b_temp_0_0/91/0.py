def find_substring(str1, sub_str):
  """
  Write a function to check if a string is present as a substring in a given list of string values.
  >>> find_substring(["red", "black", "white", "green", "orange"],"ack")==True
  """
  for i in str1:
    if sub_str in i:
      return True
  return False

def find_substring_2(str1, sub_str):
  """
  Write a function to check if a string is present as a substring in a given list of string values.
  >>> find_substring