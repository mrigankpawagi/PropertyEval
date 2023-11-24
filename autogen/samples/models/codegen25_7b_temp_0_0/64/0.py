def subject_marks(subjectmarks):
  """
  Write a function to sort a list of tuples using the second value of each tuple.
  >>> subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
  """
  return sorted(subjectmarks, key=lambda x: x[1])

def sort_list(lst):
  """
  Write a function to sort a list of tuples using the second value of each tuple.
  >>> sort_list([(2, 5), (1, 2), (4, 4), (2, 3