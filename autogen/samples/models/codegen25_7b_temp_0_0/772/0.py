def remove_length(test_str, K):
  """
  Write a function to remove all the words with k length in the given string.
  >>> remove_length('The person is most value tet', 3) == 'person is most value'
  """
  return ' '.join(word for word in test_str.split() if len(word) != K)

def remove_length_2(test_str, K):
  """
  Write a function to remove all the words with k length in the given string.
  >>> remove_length_2('The person is most value tet