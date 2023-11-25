def check_monthnumb_number(monthnum2):
  """
  Write a function to check whether the given month number contains 31 days or not.
  """
  if monthnum2 == 1 or monthnum2 == 3 or monthnum2 == 5 or monthnum2 == 7 or monthnum2 == 8 or monthnum2 == 10 or monthnum2 == 12:
    return 31
  elif monthnum2 == 4 or monthnum2 == 6 or monthnum2 == 9 or monthnum2 == 11