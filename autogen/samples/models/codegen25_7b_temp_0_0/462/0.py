def combinations_list(list1):
  """
  Write a function to find all possible combinations of the elements of a given list.
  """
  # Approach 1: Recursion
  # Time O(n*2^n)
  # Space O(n*2^n)
  def helper(list1, index, slate):
    if index == len(list1):
      res.append(slate[:])
      return
    helper(list1, index