import re
def change_date_format(dt):
  """
  Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
  """
  return dt[8:] + dt[5:7] + dt[:4]

def remove_punctuation(txt):
  """
  Write a function to remove all punctuation from a string.
  """
  return re.sub(r'[^\w\s]', '', txt)