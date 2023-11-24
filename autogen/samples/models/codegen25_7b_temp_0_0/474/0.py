def replace_char(str1,ch,newch):
  """
  Write a function to replace characters in a string.
  >>> replace_char("polygon",'y','l')==("pollgon")
  """
  return str1.replace(ch,newch)

def reverse_string(str1):
  """
  Write a function to reverse a string.
  >>> reverse_string("polygon")==("nolygon")
  """
  return str1[::-1]

def reverse_words(str1):
