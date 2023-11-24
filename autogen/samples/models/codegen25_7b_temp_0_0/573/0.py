def unique_product(list_data):
  """
  Write a python function to calculate the product of the unique numbers in a given list.
  >>> unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
  """
  unique_list = []
  for i in list_data:
    if i not in unique_list:
      unique_list.append(i)
  product = 1
  for i in unique_list:
    product *= i
  return product

def unique_product_2(list_data):
  """