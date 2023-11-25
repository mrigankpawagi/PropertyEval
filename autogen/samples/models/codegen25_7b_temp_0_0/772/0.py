def remove_length(test_str, K):
  """
  Write a function to remove all the words with k length in the given string.
  """
  words = test_str.split()
  new_words = []
  for word in words:
    if len(word) != K:
      new_words.append(word)
  return ' '.join(new_words)

print(remove_length("I am a boy", 3))

def remove_length