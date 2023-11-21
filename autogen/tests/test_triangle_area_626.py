import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
r = floats(min_value=0)

strategy = r
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def triangle_area(r) :  
    if r < 0 : 
        return None
    return r * r 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, triangle_area, *args)
