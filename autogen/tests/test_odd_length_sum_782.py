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
                
arr = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def odd_length_sum(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, odd_length_sum, *args)
