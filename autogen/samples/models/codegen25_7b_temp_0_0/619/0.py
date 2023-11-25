def move_num(test_str):
  """
  Write a function to move all the numbers to the end of the given string.
  """
  num_str = ''
  for char in test_str:
    if char.isdigit():
      num_str += char
  return test_str.replace(num_str, '') + num_str

print(move_num('abc123def456ghi789'))

def move_num(test