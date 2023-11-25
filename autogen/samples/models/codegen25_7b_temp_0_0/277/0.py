def dict_filter(dict,n):
  """
  Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
  """
  new_dict = {}
  for key, value in dict.items():
    if value >= n:
      new_dict[key] = value
  return new_dict

print(dict_filter({1:2, 2:3, 3:4, 4:5}, 3))

def dict_filter_2(