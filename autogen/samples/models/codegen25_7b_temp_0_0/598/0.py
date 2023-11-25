def armstrong_number(number):
  """
  Write a function to check whether the given number is armstrong or not.
  """
  sum = 0
  temp = number
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  return sum == number

print(armstrong_number(153))
print(armstrong_number(370))
print(armstrong_number(371))

