import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(booleans(), min_size=1)
list2 = lists(booleans(), min_size=1)
list3 = lists(booleans(), min_size=1)

strategy = list1, list2, list3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def interleave_lists(list1,list2,list3):
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, interleave_lists, *args)
