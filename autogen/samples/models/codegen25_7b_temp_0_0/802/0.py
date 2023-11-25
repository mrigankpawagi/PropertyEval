def count_rotation(arr):   
  """
  Write a python function to count the number of rotations required to generate a sorted array. https://www.geeksforgeeks.org/count-of-rotations-required-to-generate-a-sorted-array/
  """
  count = 0
  for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
      count += 1
  return count

def find_rotation_point(arr):
  """
  Write a python function to find the rotation point in a sorted array. https://www