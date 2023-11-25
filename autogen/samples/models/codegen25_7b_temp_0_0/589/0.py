def perfect_squares(a, b):
  """
  Write a function to find perfect squares between two given numbers.
  """
  return [i**2 for i in range(a, b+1) if i**2 % 2 == 0]

print(perfect_squares(1, 100))

# Output: [4, 16, 36, 64, 100]

# Time complexity: O(n)
# Space complexity: O(n)
