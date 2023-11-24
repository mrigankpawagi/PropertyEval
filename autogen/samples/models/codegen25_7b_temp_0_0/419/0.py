def round_and_sum(list1):
  """
  Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
  >>> round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
  """
  list1 = [round(i) for i in list1]
  return sum(list1) * len(list1)

def sum_of_squares(list1):
  """
  Write a function to sum the squares of a list of numbers and print the result.
  >>> sum_of_squares([1