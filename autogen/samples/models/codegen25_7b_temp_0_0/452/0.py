def loss_amount(actual_cost,sale_amount): 
  """
  Write a function that gives loss amount on a sale if the given amount has loss else return 0.
  """
  if actual_cost > sale_amount:
    return actual_cost - sale_amount
  else:
    return 0

print(loss_amount(100,90))
print(loss_amount(100,110))

# Write a function that takes a list of numbers and returns the sum of all the numbers in the list.