def dict_filter(dict,n):
  """
  Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
  >>> dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
  """
  return {k:v for k,v in dict.items() if v>=n}

def dict_reduce(dict,n):
  """
  Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values less than n.
  >>> dict_reduce({'Cierra Vega