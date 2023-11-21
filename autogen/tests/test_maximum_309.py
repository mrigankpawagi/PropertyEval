import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = integers()
b = integers()

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def maximum(a,b):   
    if a >= b: 
        return a 
    else: 
        return b 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, maximum, *args)
