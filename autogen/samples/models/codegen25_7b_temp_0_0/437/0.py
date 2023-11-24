def remove_odd(str1):
  """
  Write a function to remove odd characters in a string.
  >>> remove_odd("python")==("yhn")
  """
  str2 = ""
  for i in str1:
    if i.isdigit() == False:
      str2 += i
  return str2

def remove_odd2(str1):
  """
  Write a function to remove odd characters in a string.
  >>> remove_odd2("python")==("