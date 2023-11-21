import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = floats(min_value=0.0, exclude_min=True)
b = floats(min_value=0.0, exclude_min=True)
h = floats(min_value=0.0, exclude_min=True)

strategy = l, b, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Volume(l,b,h) : 
    return ((l * b * h) / 2) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_Volume, *args)
