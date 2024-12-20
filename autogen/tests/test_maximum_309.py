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
                
a = integers(min_value=MIN_INT, max_value=MAX_INT)
b = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def maximum(a,b):   
    if a >= b: 
        return a 
    else: 
        return b 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, maximum, *args)
