def filter_oddnumbers(nums):
  """
  Write a function to filter odd numbers.
  >>> filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
  """
  return [num for num in nums if num % 2 != 0]

def filter_evennumbers(nums):
  """
  Write a function to filter even numbers.
  >>> filter_evennumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[2,4