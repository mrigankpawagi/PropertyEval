def find_even_pair(A): 
  """
  Write a function that counts the number of pairs of integers in a list that xor to an even number.
  >>> find_even_pair([5, 4, 7, 2, 1]) == 4
  """
  count = 0
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if (A[i] ^ A[j]) % 2 == 0:
        count += 1
  return count

def find_even_pair_fast(A):
  """