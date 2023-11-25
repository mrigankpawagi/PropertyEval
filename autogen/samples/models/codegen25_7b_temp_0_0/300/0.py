def count_binary_seq(n): 
  """
  Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
  """
  if n == 0:
    return 1
  return 2**n * count_binary_seq(n-1)

def count_binary_seq_2(n):
  """
  Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits