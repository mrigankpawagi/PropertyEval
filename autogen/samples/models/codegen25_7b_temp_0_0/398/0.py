def sum_of_digits(nums):
  """
  Write a function to compute the sum of digits of each number of a given list.
  """
  return sum(int(digit) for num in nums for digit in str(num))

def sum_of_digits_2(nums):
  """
  Write a function to compute the sum of digits of each number of a given list.
  """
  return sum(int(digit) for num in nums for