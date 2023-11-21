import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lists = lists(lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN), min_size=1)

strategy = lists
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_sum_list(lists):
 return max(lists, key=sum)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_sum_list, *args)
