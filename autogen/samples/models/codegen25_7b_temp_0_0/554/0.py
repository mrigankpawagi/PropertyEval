def Split(list): 
  """
  Write a python function which takes a list of integers and only returns the odd ones.
  """
  odd_list = []
  for i in list:
    if i % 2 != 0:
      odd_list.append(i)
  return odd_list

def Reverse(list):
  """
  Write a python function which takes a list of integers and reverses it.
  """
  return list[::-