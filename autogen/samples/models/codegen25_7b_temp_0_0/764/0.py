def number_ctr(str):
  """
  Write a python function to count number of digits in a given string.
  >>> number_ctr('program2bedone') == 1
  """
  return len(re.findall(r'\d', str))

def number_ctr(str):
  """
  Write a python function to count number of digits in a given string.
  >>> number_ctr('program2bedone') == 1
  """
  return len(re.findall(r'\d