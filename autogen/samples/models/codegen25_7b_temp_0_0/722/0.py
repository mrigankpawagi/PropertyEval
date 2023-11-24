def filter_data(students,h,w):
  """
  The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
  >>> filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
  """
  return {k:v for k,v in students.items() if v[0]>=h and v[1]>=w}

def filter_data_2(students,h,w):
  """
  The input is given as - a dictionary with a student name as a key and a tuple of float (student