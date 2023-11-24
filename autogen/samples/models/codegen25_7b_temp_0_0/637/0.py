def noprofit_noloss(actual_cost,sale_amount): 
  """
  Write a function to check whether the given amount has no profit and no loss
  >>> noprofit_noloss(1500,1200)==False
  """
  if actual_cost==sale_amount:
    return True
  else:
    return False

def noprofit_loss(actual_cost,sale_amount):
  """
  Write a function to check whether the given amount has no profit but has loss
  >>> noprofit_loss(1500,1200)==