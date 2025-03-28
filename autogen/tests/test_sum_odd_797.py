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
                
l = integers(min_value=0, max_value=100)
r = integers(min_value=0, max_value=100)

strategy = l, r
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_odd(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def sum_in_range(l,r): 
    return sum_odd(r) - sum_odd(l - 1)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_odd, *args)
