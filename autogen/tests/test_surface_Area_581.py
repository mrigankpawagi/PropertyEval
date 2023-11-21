import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
b = integers(min_value=1, max_value=10)
s = integers(min_value=1, max_value=10)

strategy = b, s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def surface_Area(b,s): 
    return 2 * b * s + pow(b,2) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, surface_Area, *args)
