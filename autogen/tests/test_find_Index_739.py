import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=9)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math 
def find_Index(n): 
    x = math.sqrt(2 * math.pow(10,(n - 1)))
    return round(x)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_Index, *args)
