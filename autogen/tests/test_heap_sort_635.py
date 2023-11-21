import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
iterable = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = iterable
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq as hq
def heap_sort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, heap_sort, *args)
