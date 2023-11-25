import math
def wind_chill(v,t):
  """
  Write a function to calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in celsius.
  """
  return round((35.74 + 0.6215*t - 35.75*v**0.16 + 0.4275*t*v**0.16),0)

def wind_chill_2(v,t):
  """
  Write a function to calculate the wind chill index rounded to the next integer given the