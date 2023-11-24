def extract_string(str, l):
  """
  Write a function to extract specified size of strings from a given list of string values.
  >>> extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
  """
  return [i for i in str if len(i)==l]

def extract_string_2(str, l):
  """
  Write a function to extract specified size of strings from a given list of string values.
  >>> extract_string_2(['Python', 'list', 'exercises', 'practice', '