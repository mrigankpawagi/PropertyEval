def get_Char(strr):  
  """
  Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
  """
  sum = 0
  for i in strr:
    sum += ord(i)
  return sum % 26

def get_Char_2(strr):  
  """
  Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
  """
 