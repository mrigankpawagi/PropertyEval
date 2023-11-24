from collections import Counter 
def check_occurences(test_list):
  """
  Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
  >>> check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
  """
  return Counter(test_list)

def check_occurences_2(test_list):
  """
  Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
  >>> check_occurences_2([(3, 1), (