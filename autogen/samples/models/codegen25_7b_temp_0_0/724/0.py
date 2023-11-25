def power_base_sum(base, power):
  """
  Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
  """
  return sum(int(digit) for digit in str(base**power))

print(power_base_sum(2, 5))

def is_palindrome(string):
  """
  Write a function that takes a string as an argument and returns True if the string is a palindrome and False if it is not.