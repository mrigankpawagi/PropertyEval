import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN).flatmap(lambda l: tuples(lists(sampled_from(l), min_size=1, max_size=1), just(l)))
strategy = arr.map(lambda t: t[1] + t[0] + t[1])
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def search(arr):
    n = len(arr)
    XOR = 0
    for i in range(n) :
        XOR = XOR ^ arr[i]
    return (XOR)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, search, *args)
