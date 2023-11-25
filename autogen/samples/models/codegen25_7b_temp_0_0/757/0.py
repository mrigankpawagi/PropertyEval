def count_reverse_pairs(test_list):
  """
  Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
  """
  count = 0
  for i in range(len(test_list)):
    for j in range(i+1, len(test_list)):
      if test_list[i] == test_list[j][::-1]:
        count += 1
  return count

def count_reverse_pairs_