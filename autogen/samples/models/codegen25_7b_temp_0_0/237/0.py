from collections import Counter 
def check_occurences(test_list):
  """
  Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
  """
  # Create an empty dictionary
  occurences = {}
  # Iterate through the list of tuples
  for tuple in test_list:
    # Check if the tuple is already in the dictionary
    if tuple in occurences:
      # Increment the count if it is
      occurences[tuple] += 1