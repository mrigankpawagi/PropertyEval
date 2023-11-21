import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(tuples(integers(min_value=MIN_INT, max_value=MAX_INT), integers(min_value=MIN_INT, max_value=MAX_INT)), max_size=MAX_SEQUENCE_LEN)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def min_product_tuple(list1):
    result_min = min([abs(x * y) for x, y in list1] )
    return result_min

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, min_product_tuple, *args)
