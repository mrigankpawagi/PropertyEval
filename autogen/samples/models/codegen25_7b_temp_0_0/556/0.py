def find_Odd_Pair(A,N) : 
  """
  Write a python function to count the number of pairs whose xor value is odd.
  >>> find_Odd_Pair([5,4,7,2,1],5) == 6
  """
  count = 0
  for i in range(N) : 
    for j in range(i+1,N) : 
      if (A[i] ^ A[j]) & 1 : 
        count += 1
  return count

def find_Odd_Pair_2(A,N) : 