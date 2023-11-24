def sum_average(number):
  """
  Write a function to find sum and average of first n natural numbers.
  >>> sum_average(10)==(55, 5.5)
  """
  sum = 0
  for i in range(1, number+1):
    sum += i
  average = sum / number
  return sum, average

def sum_average_recursive(number):
  """
  Write a function to find sum and average of first n natural numbers.
  >>> sum_average_recursive