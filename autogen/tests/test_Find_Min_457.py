import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(lists(integers(min_value=MIN_INT, max_value=MAX_INT)), min_size=1)

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Find_Min(lst): 
    return min(lst, key=len) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, Find_Min, *args)
