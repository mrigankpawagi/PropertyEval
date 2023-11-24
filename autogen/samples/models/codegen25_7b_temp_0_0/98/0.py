def multiply_num(numbers):  
  """
  Write a function to multiply all the numbers in a list and divide with the length of the list.
  >>> math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
  """
  return sum(numbers) / len(numbers)

def is_palindrome(word):
  """
  Write a function to check if a word is a palindrome.
  >>> is_palindrome("madam")
  True
  >>> is_palindrome("madam, i'm mad!")