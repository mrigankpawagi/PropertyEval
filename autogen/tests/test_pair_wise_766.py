import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l1 = lists(integers())

strategy = l1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def pair_wise(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, pair_wise, *args)
