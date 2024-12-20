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
                
r = floats(min_value=0)
strategy = r
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def triangle_area(r) :  
    if r < 0 : 
        return None
    return r * r 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, triangle_area, *args)
