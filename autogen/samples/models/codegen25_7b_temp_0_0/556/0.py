def find_Odd_Pair(A,N) : 
  """
  Write a python function to count the number of pairs whose xor value is odd.
  """
  count = 0
  for i in range(0,N-1) : 
    for j in range(i+1,N) : 
      if (A[i] ^ A[j]) % 2 == 1 : 
        count += 1
  return count

def find_Odd_Pair_2(