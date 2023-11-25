from itertools import combinations 
def find_combinations(test_list):
  """
  Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
  """
  # find all combinations 
  # of three integers in list 
  # and print them 
  for i in range(0, len(test_list)): 
    for j in range(i + 1, len(test_list)): 
      for k in range(j + 1, len(test_list)