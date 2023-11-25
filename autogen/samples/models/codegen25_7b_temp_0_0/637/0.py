def noprofit_noloss(actual_cost,sale_amount): 
  """
  Write a function to check whether the given amount has no profit and no loss
  """
  if actual_cost == sale_amount:
    return True
  else:
    return False

print(noprofit_noloss(100,100))
print(noprofit_noloss(100,90))
print(noprofit_noloss(100,110))
print(n