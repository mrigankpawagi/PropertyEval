def subject_marks(subjectmarks):
  """
  Write a function to sort a list of tuples using the second value of each tuple.
  """
  return sorted(subjectmarks, key=lambda x: x[1])

def main():
  # read the input
  n = int(input())
  subjectmarks = []
  for _ in range(n):
    subjectmarks.append(tuple(input().split()))
  # sort the list of tuples
