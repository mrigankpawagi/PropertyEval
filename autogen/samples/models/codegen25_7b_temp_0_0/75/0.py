def find_tuples(test_list, K):
  """
  Write a function to find tuples which have all elements divisible by k from the given list of tuples.
  >>> find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
  """
  return [t for t in test_list if all(t[i] % K == 0 for i in range(len(t)))]

def find_tuples_2(test_list, K):
  """
  Write a function to find tuples which have all elements divisible by k from the given list of tuples.