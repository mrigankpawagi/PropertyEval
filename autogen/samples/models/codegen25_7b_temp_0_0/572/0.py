def two_unique_nums(nums):
  """
  Write a python function to remove duplicate numbers from a given number of lists.
  >>> two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
  """
  return list(set(nums))

def remove_duplicates(nums):
  """
  Write a python function to remove duplicate numbers from a given number of lists.
  >>> remove_duplicates([1,2,3,2,3,4,5]) == [1, 2, 3, 4, 5