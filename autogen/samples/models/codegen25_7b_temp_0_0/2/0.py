def similar_elements(test_tup1, test_tup2):
  """
  Write a function to find the shared elements from the given two lists.
  """
  return list(set(test_tup1) & set(test_tup2))

print(similar_elements([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

# Output: [5]

#%%
def common_elements(test_tup