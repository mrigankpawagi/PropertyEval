def sum_negativenum(nums):
  """
  Write a function to calculate the sum of the negative numbers of a given list of numbers.
  """
  sum = 0
  for num in nums:
    if num < 0:
      sum += num
  return sum

print(sum_negativenum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))