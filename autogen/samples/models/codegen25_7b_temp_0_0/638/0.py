import math
def wind_chill(v,t):
  """
  Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
  >>> wind_chill(120,35)==40
  """
  return round(35.74 + 0.6215*t - 35.75*v**0.16 + 0.4275*t*v**0.16)

def is_leap_year(year):
  """
  Write a function to determine whether a given year is a leap year.
  >>> is_le