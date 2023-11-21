import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dif_Square, *args)
