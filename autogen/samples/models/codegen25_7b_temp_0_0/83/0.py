def get_Char(strr):  
  """
  Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
  >>> get_Char("abc") == "f"
  """
  return (sum(ord(i) for i in strr) % 26)

def get_Char_2(strr):  
  """
  Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
  >>> get_Char_2("abc") == "