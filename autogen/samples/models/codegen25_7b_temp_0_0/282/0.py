def sub_list(nums1,nums2):
  """
  Write a function to subtract two lists element-wise.
  >>> sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
  """
  return [x1-x2 for x1,x2 in zip(nums1,nums2)]

def sub_list_2(nums1,nums2):
  """
  Write a function to subtract two lists element-wise.
  >>> sub_list_2([1, 2, 3],[4,