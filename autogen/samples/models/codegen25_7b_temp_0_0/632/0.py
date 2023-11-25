def move_zero(num_list):
  """
  Write a python function to move all zeroes to the end of the given list.
  """
  # TODO: Write your code here
  # return num_list
  zero_count = 0
  for i in num_list:
    if i == 0:
      zero_count += 1
  for i in range(zero_count):
    num_list.remove(0)
    num_list.append(