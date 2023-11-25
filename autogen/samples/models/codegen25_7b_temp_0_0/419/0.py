def round_and_sum(list1):
  """
  Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
  """
  list1 = [round(i) for i in list1]
  return sum(list1) * len(list1)

print(round_and_sum([1.3, 2.6, 0.5, 4.4, 4.5, 7.9, 3.3, 3.5, 6.7,