from operator import itemgetter 
def index_minimum(test_list):
  """
  Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
  >>> index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
  """
  return min(test_list, key=itemgetter(1))[0]

def index_maximum(test_list):
  """
  Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
  >>> index_maximum([('Rash', 143), ('Manje