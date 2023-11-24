import re
def change_date_format(dt):
  """
  Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
  >>> change_date_format("2026-01-02") == '02-01-2026'
  """
  return dt[8:10] + '-' + dt[5:7] + '-' + dt[0:4]

def change_date_format_2(dt):
  """
  Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
