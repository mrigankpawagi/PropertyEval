import cmath  
def convert(numbers):    
  """
  Write a python function to convert complex numbers to polar coordinates.
  """
  for number in numbers:
    print(f"The polar coordinates of {number} are:")
    print(f"The modulus is: {abs(number)}")
    print(f"The phase is: {cmath.phase(number)}")

convert([1+2j, 3+4j, 5+