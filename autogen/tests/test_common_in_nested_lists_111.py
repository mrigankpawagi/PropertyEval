import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_nested_list(draw):
    n = draw(integers(min_value=1, max_value=10))
    nested_list = draw(lists(lists(integers(), min_size=n, max_size=n), min_size=n, max_size=n))
    return nested_list

nestedlist = create_nested_list()
strategy = nestedlist
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def common_in_nested_lists(nestedlist):
    result = list(set.intersection(*map(set, nestedlist)))
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, common_in_nested_lists, *args)
