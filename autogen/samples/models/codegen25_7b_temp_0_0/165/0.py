def count_char_position(str1): 
  """
  Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
  """
  count = 0
  for i in range(len(str1)):
    if str1[i].lower() == chr(i+97):
      count += 1
  return count

print(count_char_position("Hello"))

def count_char_position_2(str1):
  """
 