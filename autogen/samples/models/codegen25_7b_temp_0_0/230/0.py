def replace_blank(str1,char):
  """
  Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
  """
  return str1.replace(" ","_")

def replace_blank_2(str1,char):
  """
  Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
  """
  return "".join(char if x==" " else x for