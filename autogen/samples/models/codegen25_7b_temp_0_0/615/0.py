def average_tuple(nums):
  """
  Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
  """
  return [sum(x)/len(x) for x in zip(*nums)]

def average_tuple_2(nums):
  """
  Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
  """
  return [sum(x)/len(x) for