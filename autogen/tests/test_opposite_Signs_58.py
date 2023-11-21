import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
x = integers()
y = integers()

strategy = x, y
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def opposite_Signs(x,y): 
    return ((x ^ y) < 0); 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, opposite_Signs, *args)
