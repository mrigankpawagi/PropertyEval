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

def is_Sum_Of_Powers_Of_Two(n): 
    if (n % 2 == 1): 
        return False
    else: 
        return True

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_Sum_Of_Powers_Of_Two, *args)
