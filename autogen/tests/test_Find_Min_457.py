import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Find_Min(lst): 
    return min(lst, key=len) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, Find_Min, *args)
