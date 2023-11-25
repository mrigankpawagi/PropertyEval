import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
actual_cost = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)
sale_amount = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)

@given(actual_cost, sale_amount)
def loss_amount(actual_cost, sale_amount):
    if actual_cost > sale_amount:
        return actual_cost - sale_amount
    return 0

strategy = loss_amount
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def loss_amount(actual_cost,sale_amount): 
  if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    return amount
  else:
    return 0

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, loss_amount, *args)
