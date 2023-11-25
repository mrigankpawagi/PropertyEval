import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l1 = lists(elements=integers(), max_size=MAX_SEQUENCE_LEN)
l2 = lists(elements=integers(), max_size=MAX_SEQUENCE_LEN)
l3 = lists(elements=integers(), max_size=MAX_SEQUENCE_LEN)

strategy = l1, l2, l3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_index_list(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_index_list, *args)
