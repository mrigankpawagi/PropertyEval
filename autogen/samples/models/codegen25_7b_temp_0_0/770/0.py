def odd_num_sum(n) : 
  """
  Write a python function to find the sum of fourth power of first n odd natural numbers.
  """
  sum = 0
  for i in range(1, n+1, 2) : 
    sum += i**4
  return sum

print(odd_num_sum(10))

# Write a python function to find the sum of fifth power of first n odd natural numbers.
def odd_num_sum(n)