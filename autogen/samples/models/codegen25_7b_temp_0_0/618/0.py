def div_list(nums1,nums2):
  """
  Write a function to divide two lists element wise.
  >>> div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
  """
  return [nums1[i]/nums2[i] for i in range(len(nums1))]

def div_list_2(nums1,nums2):
  """
  Write a function to divide two lists element wise.
  >>> div_list_2([4,5,6],[