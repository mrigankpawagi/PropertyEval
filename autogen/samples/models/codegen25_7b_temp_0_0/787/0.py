import re
def text_match_three(text):
  """
  Write a function that matches a string that has an a followed by three 'b'.
  """
  pattern = re.compile(r'ab{3}')
  result = re.findall(pattern, text)
  return result

print(text_match_three("ababababab"))
print(text_match_three("abababababababababababababababababab