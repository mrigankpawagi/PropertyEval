import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def unique_Element(arr):
    s = set(arr)
    return len(s) == 1

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, unique_Element, *args)
