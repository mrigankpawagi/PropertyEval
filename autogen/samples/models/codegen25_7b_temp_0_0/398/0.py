def sum_of_digits(nums):
  """
  Write a function to compute the sum of digits of each number of a given list.
  >>> sum_of_digits([10,2,56])==14
  """
  return sum([int(i) for i in str(nums)])

def sum_of_digits_2(nums):
  """
  Write a function to compute the sum of digits of each number of a given list.
  >>> sum_of_digits_2([10,2,56])==14
