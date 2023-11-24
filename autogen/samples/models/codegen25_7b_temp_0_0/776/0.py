def count_vowels(test_str):
  """
  Write a function to count those characters which have vowels as their neighbors in the given string.
  >>> count_vowels('bestinstareels') == 7
  """
  vowels = ['a', 'e', 'i', 'o', 'u']
  count = 0
  for i in range(len(test_str)):
    if test_str[i] in vowels:
      if i == 0:
        count += 1
      elif test_str[i-1]