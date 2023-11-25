import re
def replace_specialchar(text):
  """
  Write a function to replace all occurrences of spaces, commas, or dots with a colon.
  """
  text = text.replace(" ", ":")
  text = text.replace(",", ":")
  text = text.replace(".", ":")
  return text

def remove_specialchar(text):
  """
  Write a function to remove all occurrences of spaces, commas, or dots.
  """
