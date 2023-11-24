def check_monthnumber_number(monthnum3):
  """
  Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
  >>> check_monthnumber_number(6)==True
  """
  if monthnum3==1 or monthnum3==3 or monthnum3==5 or monthnum3==7 or monthnum3==8 or monthnum3==10 or monthnum3==12:
    return True
  elif monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11