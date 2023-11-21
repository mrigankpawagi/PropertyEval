import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(lists(integers(), min_size=2, max_size=2), min_size=1)

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def merge(lst):  
    return [list(ele) for ele in list(zip(*lst))] 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, merge, *args)
