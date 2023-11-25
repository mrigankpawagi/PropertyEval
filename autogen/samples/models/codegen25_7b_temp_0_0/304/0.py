def find_Element(arr,ranges,rotations,index) :  
  """
  Write a python function to find element at a given index after number of rotations.
  """
  if index >= ranges :
    return arr[index%ranges]
  else :
    return arr[index]

def find_Element_2(arr,ranges,rotations,index) :  
  """
  Write a python function to find element at a given index after number of rotations.
  """
 