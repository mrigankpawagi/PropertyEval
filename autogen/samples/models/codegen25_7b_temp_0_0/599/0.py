def sum_average(number):
  """
  Write a function to find sum and average of first n natural numbers.
  """
  sum = 0
  for i in range(1, number+1):
    sum += i
  average = sum / number
  return sum, average

print(sum_average(10))

def sum_average_recursive(number):
  """
  Write a function to find sum and average of first n natural numbers