import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
actual_cost = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT, allow_nan=False)
sale_amount = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT, allow_nan=False)

strategy = actual_cost, sale_amount
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def noprofit_noloss(actual_cost,sale_amount): 
  if(sale_amount == actual_cost):
    return True
  else:
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, noprofit_noloss, *args)
