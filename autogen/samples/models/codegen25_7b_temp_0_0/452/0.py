def loss_amount(actual_cost,sale_amount): 
  """
  Write a function that gives loss amount on a sale if the given amount has loss else return 0.
  >>> loss_amount(1500,1200)==0
  """
  if actual_cost > sale_amount:
    return actual_cost - sale_amount
  else:
    return 0

def loss_percentage(actual_cost,sale_amount):
  """
  Write a function that gives loss percentage on a sale if the given amount has loss else return 0.
  >>> loss_percent