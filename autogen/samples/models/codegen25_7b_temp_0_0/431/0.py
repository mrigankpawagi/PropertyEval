def common_element(list1, list2):
  """
  Write a function that takes two lists and returns true if they have at least one common element.
  >>> common_element([1,2,3,4,5], [5,6,7,8,9])==True
  """
  for i in list1:
    if i in list2:
      return True
  return False

def is_palindrome(string):
  """
  Write a function that takes a string and determines if it is a palindrome.
  >>> is_palindrome("racecar")==True
  """
 