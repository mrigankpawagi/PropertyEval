import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
b = floats(min_value=0.0, max_value=MAX_FLOAT)
h = floats(min_value=0.0, max_value=MAX_FLOAT)

strategy = b, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def surface_Area(b,s): 
    return 2 * b * s + pow(b,2) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, surface_Area, *args)
