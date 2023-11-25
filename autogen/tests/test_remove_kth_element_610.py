import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(integers(), min_size=1, unique=True)
L = integers(min_value=0)

strategy = list1, L
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_kth_element(list1, L):
    return  list1[:L-1] + list1[L:]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_kth_element, *args)
