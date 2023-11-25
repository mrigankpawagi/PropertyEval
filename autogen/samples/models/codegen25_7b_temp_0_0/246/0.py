def babylonian_squareroot(number):
  """
  Write a function for computing square roots using the babylonian method.
  """
  # Initialize the guess and the counter
  guess = number / 2
  counter = 0

  # Loop until the guess is accurate enough
  while guess * guess != number:
    guess = (guess + number / guess) / 2
    counter += 1

  return guess, counter

def main():
  print(b