def mul_even_odd(list1):
  """
  Write a function to find the product of first even and odd number of a given list.
  """
  even_product = 1
  odd_product = 1
  for i in range(len(list1)):
    if i % 2 == 0:
      even_product *= list1[i]
    else:
      odd_product *= list1[i]
  return even_product, odd_product

