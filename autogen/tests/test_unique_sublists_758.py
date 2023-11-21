import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(lists(integers(), min_size=1), min_size=1)

@composite
def create_list(draw):
    l = draw(lists(draw(lists(integers())), min_size=1))
    return l

list1 = create_list()

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
