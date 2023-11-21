import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(lists(booleans(), min_size=1, max_size=10), min_size=1, max_size=10)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def unique_sublists(list1):
    result ={}
    for l in  list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, unique_sublists, *args)
