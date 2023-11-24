def average_tuple(nums):
  """
  Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
  >>> average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
  """
  return [sum(i)/len(i) for i in nums]

def average_tuple_2(nums):
  """
  Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
  >>> average_tuple_2(((10, 10, 10, 12