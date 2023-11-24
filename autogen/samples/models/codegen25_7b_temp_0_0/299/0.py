from collections import defaultdict
def max_aggregate(stdata):
  """
  Write a function to calculate the maximum aggregate from the list of tuples.
  >>> max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
  """
  max_aggregate = 0
  for i in stdata:
    if i[1] > max_aggregate:
      max_aggregate = i[1]
  for i in stdata:
    if i[1] == max_aggregate:
      return i

def max_aggregate_dict(st