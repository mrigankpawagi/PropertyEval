def intersection_array(array_nums1,array_nums2):
  """
  Write a function to find the intersection of two arrays.
  >>> intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
  """
  return list(set(array_nums1) & set(array_nums2))

def intersection_array_2(array_nums1,array_nums2):
  """
  Write a function to find the intersection of two arrays.
  >>> intersection_array_2([1, 2, 3, 5,