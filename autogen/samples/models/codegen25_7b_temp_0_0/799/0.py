def left_rotate(n,d):   
  """
  Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
  >>> left_rotate(16,2) == 64
  """
  return (n << d) | (n >> (32-d))

def right_rotate(n,d):
  """
  Write a function to that rotate right bits by d bits a given number. We assume that the number is 32 bit.
  >>> right_rotate(16,2) == 32
  """
