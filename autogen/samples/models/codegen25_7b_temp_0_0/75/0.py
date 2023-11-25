def find_tuples(test_list, K):
  """
  Write a function to find tuples which have all elements divisible by k from the given list of tuples.
  """
  result = []
  for i in test_list:
    if all(j % K == 0 for j in i):
      result.append(i)
  return result

print(find_tuples([(1, 2, 3), (2, 4, 6), (3, 6, 9)], 6))

