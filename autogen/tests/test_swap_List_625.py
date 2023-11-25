import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
newList = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN)
strategy = newList
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def swap_List(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, swap_List, *args)
