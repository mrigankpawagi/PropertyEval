import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def tuple_list(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    lst = draw(lists(tuples(integers(), integers()), min_size=n, max_size=n))
    return lst

lst = tuple_list()
strategy = lst
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
