def mul_even_odd(list1):
  """
  Write a function to find the product of first even and odd number of a given list.
  >>> mul_even_odd([1,3,5,7,4,1,6,8])==4
  """
  even_num = 0
  odd_num = 0
  for i in list1:
    if i % 2 == 0:
      even_num = even_num * i
    else:
      odd_num = odd_num * i
  return even_num * odd_num

def sum_of_even_