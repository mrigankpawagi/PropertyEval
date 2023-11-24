def get_ludic(n):
  """
  Write a function to get all lucid numbers smaller than or equal to a given integer.
  >>> get_ludic(10) == [1, 2, 3, 5, 7]
  """
  if n < 1:
    return []
  return [1] + [i for i in range(2, n + 1) if not any(i % j == 0 for j in range(2, i))]

def get_ludic_sum(n):
  """
  Write a function to get the sum of all