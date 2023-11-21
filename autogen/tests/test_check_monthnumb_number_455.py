import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
monthnum2 = integers(min_value=1, max_value=12)

strategy = monthnum2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_monthnumb_number(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_monthnumb_number, *args)
