def find_Element(arr,ranges,rotations,index) :  
  """
  Write a python function to find element at a given index after number of rotations.
  >>> find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
  """
  if index >= ranges[rotations][0] and index <= ranges[rotations][1] :
    return arr[index]
  else :
    return -1

def find_Element_2(arr,ranges,rotations,index) :  
  """
  Write a python function to find element at a given index