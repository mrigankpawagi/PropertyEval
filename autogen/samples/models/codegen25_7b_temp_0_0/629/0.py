def Split(list): 
  """
  Write a python function to find even numbers from a list of numbers.
  >>> Split([1,2,3,4,5]) == [2,4]
  """
  even_numbers = []
  for i in list:
    if i % 2 == 0:
      even_numbers.append(i)
  return even_numbers

def Split_2(list):
  """
  Write a python function to find even numbers from a list of numbers.
  >>> Split_2