import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_tuple_list(draw):
    n = draw(integers(min_value=1, max_value=100))
    return draw(lists(tuples(text(), integers(min_value=0, max_value=100)), min_size=n, max_size=n))

tuples_list = create_tuple_list()

strategy = tuples_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import defaultdict
def max_aggregate(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_aggregate, *args)
