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
                
l = floats(min_value=1, max_value=100)
b = floats(min_value=1, max_value=100)
h = floats(min_value=1, max_value=100)

strategy = l, b, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Volume(l,b,h) : 
    return ((l * b * h) / 2) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_Volume, *args)
