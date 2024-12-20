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
                
n = integers(min_value=0, max_value=2**32-1)
d = integers(min_value=0, max_value=31)

strategy = n, d
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def left_rotate(n,d):   
    INT_BITS = 32
    return (n << d)|(n >> (INT_BITS - d))  

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, left_rotate, *args)
