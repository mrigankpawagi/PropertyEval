def move_num(test_str):
  """
  Write a function to move all the numbers to the end of the given string.
  >>> move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
  """
  return ''.join(sorted(test_str, key=lambda x: x.isdigit()))

def move_num(test_str):
  """
  Write a function to move all the numbers to the end of the given string.
  >>> move_num('I1love143you55three3000thousand')