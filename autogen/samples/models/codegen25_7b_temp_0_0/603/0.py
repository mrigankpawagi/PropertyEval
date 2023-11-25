def get_ludic(n):
  """
  Write a function to get all lucid numbers smaller than or equal to a given integer.
  """
  if n < 1:
    return []
  return [x for x in range(1, n + 1) if is_ludic(x)]

def is_ludic(n):
  """
  Write a function to check if a number is a ludic number.
  """
  if n < 1:
   