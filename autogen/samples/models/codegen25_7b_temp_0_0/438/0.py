def count_bidirectional(test_list):
  """
  Write a function to count bidirectional tuple pairs.
  """
  count = 0
  for i in range(len(test_list)):
    for j in range(i + 1, len(test_list)):
      if test_list[i][1] == test_list[j][0]:
        count += 1
  return count

def count_bidirectional_2