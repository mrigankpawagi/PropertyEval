def reverse_string_list(stringlist):
  """
  Write a function to reverse each string in a given list of string values.
  """
  return [s[::-1] for s in stringlist]

def reverse_string_list_recursive(stringlist):
  """
  Write a function to reverse each string in a given list of string values.
  """
  if len(stringlist) == 0:
    return []
  return [stringlist[