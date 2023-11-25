import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(booleans() | floats() | integers() | text(), min_size=0, max_size=10)
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def combinations_list(list1):
    if len(list1) == 0:
        return [[]]
    result = []
    for el in combinations_list(list1[1:]):
        result += [el, el+[list1[0]]]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, combinations_list, *args)
