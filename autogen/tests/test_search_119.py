import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=3, average_size=10).map(sorted)

strategy = arr
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
