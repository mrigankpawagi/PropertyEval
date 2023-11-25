import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
N = integers(min_value=0, max_value=MAX_INT)

strategy = N
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math  
def next_Perfect_Square(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, next_Perfect_Square, *args)
