def all_Characters_Same(s) :
  """
  Write a python function to check whether all the characters are same or not.
  >>> all_Characters_Same("python") == False
  """
  if len(s) == 0 :
    return True
  else :
    return s[0] == s[-1] and all_Characters_Same(s[1:-1])

def all_Characters_Same_2(s) :
  """
  Write a python function to check whether all the characters are same or