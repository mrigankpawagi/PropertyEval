import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
l1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
l2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
l3 = lists(integers(), max_size=MAX_SEQUENCE_LEN)

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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, extract_index_list, *args)
