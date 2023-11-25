def reverse_words(s):
  """
  Write a function to reverse words seperated by spaces in a given string.
  """
  # split the string into words
  words = s.split(" ")
  # reverse the words
  words = words[::-1]
  # join the words back together
  return " ".join(words)

print(reverse_words("The quick brown fox jumps over the lazy dog"))

# Write a function to