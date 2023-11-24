def move_zero(num_list):
  """
  Write a python function to move all zeroes to the end of the given list.
  >>> move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
  """
  return [i for i in num_list if i != 0] + [0] * num_list.count(0)

def move_zero_2(num_list):
  """
  Write a python function to move all zeroes to the end of the given list.
  >>> move_zero_2([1,