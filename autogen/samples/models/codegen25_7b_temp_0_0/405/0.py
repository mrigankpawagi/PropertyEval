def check_tuplex(tuplex,tuple1): 
  """
  Write a function to check whether an element exists within a tuple.
  """
  for i in tuplex:
    if i == tuple1:
      return True
  return False

print(check_tuplex((1,2,3,4,5),4))

def check_tuplex(tuplex,tuple1): 
  """
  Write a function to check whether