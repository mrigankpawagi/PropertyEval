from collections import deque
def check_expression(exp):
  """
  Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
  >>> check_expression("{()}[{}]") == True
  """
  stack = deque()
  for char in exp:
    if char == '{' or char == '(' or char == '[':
      stack.append(char)
    elif char == '}' or char == ')' or char == ']':
      if not stack:
        return False
      last_char =