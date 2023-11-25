import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
  """
  Write a function to check whether the given string starts and ends with the same character or not.
  """
  if re.match(regex, string): 
    return True
  else: 
    return False

print(check_char("a"))
print(check_char("ab"))
print(check_char("abb"))
print(check_char("abbb"))
print(check_char("abbbb"))
print