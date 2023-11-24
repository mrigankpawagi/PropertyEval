def sum_negativenum(nums):
  """
  Write a function to calculate the sum of the negative numbers of a given list of numbers.
  >>> sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
  """
  sum = 0
  for num in nums:
    if num < 0:
      sum += num
  return sum

def sum_evennum(nums):
  """
  Write a function to calculate the sum of the even numbers of a given list of numbers.
  >>> sum_evennum([2, 4, -