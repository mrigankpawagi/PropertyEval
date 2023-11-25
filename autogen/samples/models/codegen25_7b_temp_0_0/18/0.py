NO_OF_CHARS = 256
def str_to_list(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 
def lst_to_string(List): 
	return ''.join(List) 
def get_char_count_array(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def remove_dirty_chars(string, second_string): 
  """
  Write a function to remove characters from the first string which are present in the second string.
  """
  for i in second_string: 
    string = string.replace(i, "") 
  return string 
def remove_duplicate_chars(string): 
	"""
	Write a function to remove duplicate characters from the given string.
	"""
	for i in range(len(string)): 
