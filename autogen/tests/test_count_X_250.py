import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
tup = tuples(integers())
x = integers()

strategy = tup, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_X(tup, x): 
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_X, *args)
