def filter_data(students,h,w):
  """
  The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
  """
  filtered_students = {}
  for student in students:
    if students[student][0] > h and students[student][1] > w:
      filtered_students[student] = students[student]
  return filtered_students

students = {
  "Harry": (37.21, 19.53