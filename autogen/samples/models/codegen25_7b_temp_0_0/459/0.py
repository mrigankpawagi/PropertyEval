import re
def remove_uppercase(str1):
  """
  Write a function to remove uppercase substrings from a given string.
  >>> remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
  """
  return re.sub(r'[A-Z]', '', str1)

def remove_digits(str1):
  """
  Write a function to remove digits from a given string.
  >>> remove_digits('cAstyoUrFavoRitETVshoWs') == 'cAstyoUr