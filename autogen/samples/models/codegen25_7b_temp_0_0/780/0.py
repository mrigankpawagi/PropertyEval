from itertools import combinations 
def find_combinations(test_list):
  """
  Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
  >>> find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
  """
  result = []
  for i in range(len(test_list)):
    for j in range(i+1, len(test_list)):
      for k in range(j+1, len(test_list)):
        result.append(tuple(sorted(test_list[i] + test_