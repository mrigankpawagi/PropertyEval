import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
  """
  Write a function to check whether the given string starts and ends with the same character or not.
  >>> check_char("abba") == "Valid"
  """
  if re.match(regex, string):
    return "Valid"
  else:
    return "Invalid"

def check_char_2(string):
  """
  Write a function to check whether the given string starts and ends with the same character or not.
  >>> check_char_2("abba") == "