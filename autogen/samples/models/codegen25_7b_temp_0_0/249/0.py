def intersection_array(array_nums1,array_nums2):
  """
  Write a function to find the intersection of two arrays.
  """
  # Time O(n) || Space O(n)
  if len(array_nums1) == 0 or len(array_nums2) == 0:
    return []
  hashTable = {}
  for num in array_nums1:
    hashTable[num] = True
  result = []
 