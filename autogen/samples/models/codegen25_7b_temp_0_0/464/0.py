def check_value(dict, n):
  """
  Write a function to check if all values are same in a dictionary.
  >>> check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
  """
  return all(dict[key] == n for key in dict)

def check_value_2(dict, n):
  """
  Write a function to check if all values are same in a dictionary.
  >>> check_value_2({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra