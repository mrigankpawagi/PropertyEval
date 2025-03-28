import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
n = integers(min_value=1, max_value=10)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def cube_Sum(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, cube_Sum, *args)
