def check_integer(text):
  """
  Write a function to check if a string represents an integer or not.
  >>> check_integer("python")==False
  """
  try:
    int(text)
    return True
  except ValueError:
    return False

def check_float(text):
  """
  Write a function to check if a string represents a float or not.
  >>> check_float("python")==False
  """
  try:
    float(text)