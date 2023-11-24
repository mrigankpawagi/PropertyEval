def power_base_sum(base, power):
  """
  Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
  >>> power_base_sum(2,100)==115
  """
  return sum([int(i) for i in str(base**power)])

def is_palindrome(string):
  """
  Write a function that takes a string as argument and returns True if the string is a palindrome and False if it is not.
  >>> is_palindrome("madam")
 