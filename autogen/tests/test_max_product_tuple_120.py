import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(tuples(integers(), integers()), min_size=1, max_size=10)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_product_tuple(list1):
    result_max = max([abs(x * y) for x, y in list1] )
    return result_max

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_product_tuple, *args)
