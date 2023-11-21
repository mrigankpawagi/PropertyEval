import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nestedlist = lists(lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN),
                   min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = nestedlist
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def common_in_nested_lists(nestedlist):
    result = list(set.intersection(*map(set, nestedlist)))
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, common_in_nested_lists, *args)
