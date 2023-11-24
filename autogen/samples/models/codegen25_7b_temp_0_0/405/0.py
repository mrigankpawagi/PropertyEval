def check_tuplex(tuplex,tuple1): 
  """
  Write a function to check whether an element exists within a tuple.
  >>> check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
  """
  return tuple1 in tuplex

def convert_int_bin(num):
  """
  Write a function to convert a base-10 integer to binary representation.
  >>> convert_int_bin(5)=='101'
  """
  return bin(num)[2:]

def convert_int_hex(num