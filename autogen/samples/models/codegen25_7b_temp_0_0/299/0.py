from collections import defaultdict
def max_aggregate(stdata):
  """
  Write a function to calculate the maximum aggregate from the list of tuples.
  """
  # Create a dictionary to store the maximum aggregate
  max_aggregate = defaultdict(int)
  # Iterate through the list of tuples
  for i in stdata:
    # Iterate through the tuple
    for j in i:
      # If the value is greater than the current value
      if j > max_