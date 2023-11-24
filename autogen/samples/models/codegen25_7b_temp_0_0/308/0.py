def large_product(nums1, nums2, N):
  """
  Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
  >>> large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
  """
  return [max(nums1[i]*nums2[i], nums1[i]*nums2[i+1], nums1[i]*nums2[i+2], nums1[i+1]*nums2[i], nums1[i+1]*nums2