from collections import deque
def check_expression(exp):
  """
  Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
  """
  stack = deque()
  for i in exp:
    if i == '(':
      stack.append(i)
    elif i == ')':
      if len(stack) == 0:
        return False
      stack.pop()
  if len(stack) == 0:
    return True
  return False