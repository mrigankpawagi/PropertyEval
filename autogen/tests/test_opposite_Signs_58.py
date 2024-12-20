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
                
x = integers(min_value=MIN_INT, max_value=MAX_INT)
y = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = x, y
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def opposite_Signs(x,y): 
    return ((x ^ y) < 0); 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, opposite_Signs, *args)
